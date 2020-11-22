from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.


class ModeloBase (models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Roles(models.Model):
    Cliente = 1
    Proveedor = 2
    Vendedor = 3
    Supervisor = 4
    Admin = 5
    TIPOS_ROLES = (
        (Cliente, "CLIENTE"),
        (Proveedor, "PROVEEDOR"),
        (Vendedor, "VENDEDOR"),
        (Supervisor, "SUPERVISOR"),
        (Admin, "ADMIN"),

    )
    id = models.PositiveSmallIntegerField(choices=TIPOS_ROLES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class UserManager (BaseUserManager):
    def create_user(
        self,
        nombre_usuario,
        identidad,
        primer_nombre,
        primer_apellido,
        fecha_nacimiento,
        genero,
        password=None,

    ):
        if (
            not identidad
            or not nombre_usuario
            or not primer_nombre
            or not primer_apellido
            or not fecha_nacimiento
            or not genero
        ):
            raise ValueError("Asegurese de llenar todos los campos")

        user = self.model(
            password=password,
            nombre_usuario=nombre_usuario,
            identidad=identidad,
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        nombre_usuario,
        identidad,
        primer_nombre,
        primer_apellido,
        fecha_nacimiento,
        genero,
        password,
    ):
        usuario = self.create_user(
            password=password,
            nombre_usuario=nombre_usuario,
            identidad=identidad,
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,

        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    MASCULINO = "M"
    FEMENINO = "F"
    GENERO = [(MASCULINO, "Masculino"), (FEMENINO, "Femenino")]
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    identidad = models.CharField(max_length=13, unique=True)
    primer_nombre = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10, choices=GENERO, null=True)
    correo = models.EmailField(max_length=254, unique=False, blank=True, null=True)
    telefono = models.CharField(max_length=8)
    cedula = models.CharField(max_length=13)
    rtn = models.CharField(max_length=14)
    creacion = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length=50)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "nombre_usuario"
    REQUIRED_FIELDS = [
        "identidad",
        "primer_nombre",
        "fecha_nacimiento",
        "genero"
    ]


class TipoProducto (models.Model):
    Abarroteria = 1
    Repuestos = 2
    Comida = 3

    TIPOS_PRODUCTOS = (
        (Abarroteria, "ABARROTERIA"),
        (Repuestos, "REPUESTOS"),
        (Comida, "COMIDA")

    )
    id = models.PositiveSmallIntegerField(choices=TIPOS_PRODUCTOS, primary_key=True)

    def __str__(self):
        return self.get_id_display()

class Producto(ModeloBase):
    id = models.AutoField(primary_key=True)
    tipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    marca = models.CharField(max_length=50)
    isv = models.DecimalField(max_digits=5, decimal_places=2)
    nombrePopular = models.CharField(max_length=50, null=True)
    descripcionProducto = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombreProducto


class Pedido (ModeloBase):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Usuario, related_name='Proveedor', on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ENCURSO = "E"
    PAGADO = "P"
    ESTADOPEDIDO = [(ENCURSO, "En Curso"), (PAGADO, "Pagado")]
    estadoPedido = models.CharField(max_length=10, choices=ESTADOPEDIDO, null=True)


class Inventario (ModeloBase):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    precioCosto = models.DecimalField(max_digits=5, decimal_places=2)
    precioVenta = models.DecimalField(max_digits=5, decimal_places=2)
    existencia = models.IntegerField(null=True, blank=True)


class Entrada (ModeloBase):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    DEVOLUCION = "D"
    COMPRA = "C"
    TIPOENTRADA = [(DEVOLUCION, "Devolucion"), (COMPRA, "Compra")]
    estadoPedido = models.CharField(max_length=10, choices=TIPOENTRADA, null=True)
    fecha = models.DateField
    precioCosto = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField
    numeroFactura = models.CharField(max_length=100)




class Factura (ModeloBase):
    id = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Usuario, related_name='Cliente', on_delete=models.CASCADE)
    Vendedor = models.OneToOneField(Usuario, related_name='Vendedor', on_delete=models.CASCADE, null=True, blank=True)
    nombreCliente = models.CharField(max_length=20, null=True, blank=True)
    rtn = models.CharField(max_length=14)
    numero = models.CharField(max_length=9, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class Descuento (ModeloBase):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class FacturaDetalle (ModeloBase):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE, null=True, blank=True)
    descipcion = models.CharField(max_length=50)
    cantidad = models.IntegerField
    valorUnitario = models.DecimalField(max_digits=5, decimal_places=2)


class Salida (models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    CREDITO = "CRE"
    CONTADO = "CON"
    tipoSal = [(CREDITO, "Credito"), (CONTADO, "Contado")]
    tipoSalida = models.CharField(max_length=10, choices=tipoSal, null=True)
    fecha = models.DateField(null=True, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField




