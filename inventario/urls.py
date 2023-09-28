from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)

urlpatterns = [
    path("contact/<str:name>", views.contact, name="index"),
    # path("categorias/", views.categorias, name="categorias"),
    path("productos/", views.productFormView, name="productos"),
    # path("", views.index, name="index"),
    path('categorias/crear/', views.CategoriasCreateView.as_view(), name='categorias'),
    path('categorias/cantidad/', views.categoria_count, name='categorias_cantidad'),
    path('productos/filtrar/unidades/', views.productos_en_unidades, name='productos_en_unidades'),
    path('reporte/productos/', views.reporte_productos),
    path("", include(router.urls)),
]
