from django.urls import path
from .views import (AddBrandView,
    AddCategoryView,
    BrandListView,
    CategoryListView,
    DeleteBrandView,
    DeleteCategoryView,
    HomeView,
    ItemListView,
    AddItemView,
    DeleteItemView,
    LogoutView,
    UpdateBrandView,
    UpdateCategoryView,
    UpdateItemView,
    AdminLogin,
    ValidateCategoryView)


app_name = "inventory"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("item-list/", ItemListView.as_view(), name="item_list"),
    path("add-item/", AddItemView.as_view(), name="add_item"),
    path("delete-item/<int:id>/", DeleteItemView.as_view(), name="delete_item"),
    path("update-item/<int:id>/", UpdateItemView.as_view(), name="update-item"),
    path("category-list/", CategoryListView.as_view(), name="category_list"),
    path("add-category/", AddCategoryView.as_view(), name="add_category"),
    path("category/validate-name/",ValidateCategoryView.as_view(), name="validate_category_name"),
    path("delete-category/<int:id>/", DeleteCategoryView.as_view(), name="delete_category"),
    path("update-category/<int:id>/", UpdateCategoryView.as_view(), name="update_category"),
    path("brand-list/", BrandListView.as_view(), name="brand_list"),
    path("add-brand/", AddBrandView.as_view(), name="add_brand"),
    path("delete-brand/<int:id>/", DeleteBrandView.as_view(), name="delete_brand"),
    path("update-brand/<int:id>/", UpdateBrandView.as_view(), name="update_brand"),
    path("login/", AdminLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

]