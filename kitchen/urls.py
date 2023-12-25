from django.urls import path

from kitchen.views import DishTypeListView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView, DishListView, \
    DishDetailView, DishCreateView, DishUpdateView, DishDeleteView, index

urlpatterns = [
    path("", index, name="index"),
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
    path("dishes/", DishListView.as_view(), name="car-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="car-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="car-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="car-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="car-delete"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-car-assign",
    ),
    path("cookers/", CookListView.as_view(), name="driver-list"),
    path(
        "cookers/<int:pk>/", CookDetailView.as_view(), name="driver-detail"
    ),
    path("cookers/create/", CookCreateView.as_view(), name="driver-create"),
    path(
        "cookers/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="driver-update",
    ),
    path(
        "cookers/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="driver-delete",
    ),
]

app_name = "taxi"
