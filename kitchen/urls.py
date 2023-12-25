from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishtype/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "dishtype/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "dishtype/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "dishtype/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),
    path("dishes/", CarListView.as_view(), name="car-list"),
    path("dishes/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("dishes/create/", CarCreateView.as_view(), name="car-create"),
    path("dishes/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("dishes/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_assign_to_car,
        name="toggle-car-assign",
    ),
    path("cookers/", DriverListView.as_view(), name="driver-list"),
    path(
        "cookers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path("cookers/", DriverListView.as_view(), name="driver-list"),
    path(
        "cookers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path("cookers/create/", DriverCreateView.as_view(), name="driver-create"),
    path(
        "cookers/<int:pk>/update/",
        DriverLicenseUpdateView.as_view(),
        name="driver-update",
    ),
    path(
        "cookers/<int:pk>/delete/",
        DriverDeleteView.as_view(),
        name="driver-delete",
    ),
]

app_name = "taxi"
