from django.urls import path

from kitchen.views import (DishTypeListView,
                           DishTypeCreateView,
                           DishTypeUpdateView,
                           DishTypeDeleteView,
                           DishListView,
                           DishDetailView,
                           DishCreateView,
                           DishUpdateView,
                           DishDeleteView,
                           IndexView,
                           CookDetailView,
                           CookListView,
                           CookCreateView,
                           CookExperienceUpdateView,
                           CookDeleteView,
                           DishToggleAssign)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "dishtype/",
        DishTypeListView.as_view(),
        name="dishtype-list",
    ),
    path(
        "dishtype/create/",
        DishTypeCreateView.as_view(),
        name="dishtype-create",
    ),
    path(
        "dishtype/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dishtype-update",
    ),
    path(
        "dishtype/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dishtype-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        DishToggleAssign.delete,
        name="toggle-dish-assign",
    ),
    path("cookers/", CookListView.as_view(), name="cook-list"),
    path(
        "cookers/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path("cookers/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cookers/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cookers/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
]

app_name = "kitchen"
