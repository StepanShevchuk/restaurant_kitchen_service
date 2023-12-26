from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import DishType, Dish, Cook
from .forms import (
    CookCreationForm,
    CookExperienceUpdateForm,
    DishForm,
    DishTypeSearchForm,
    DishSearchForm,
    CookSearchForm
)



def index(request):
    """View function for the home page of the site."""

    num_cookers = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dishtypes = DishType.objects.count()

    context = {
        "num_cookers": num_cookers,
        "num_dishes": num_dishes,
        "num_dishtypes": num_dishtypes,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dishtype_list"
    template_name = "kitchen/dishtype_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = DishTypeSearchForm
        return context

    def get_queryset(self):
        if self.request.GET.get("name"):
            return DishType.objects.filter(
                name__icontains=self.request.GET.get("name"))
        return DishType.objects.all()


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "kitchen/dishtype_create.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "kitchen/dishtype_update.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "kitchen/dishtype_delete.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = "kitchen/dish_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = DishSearchForm
        return context

    def get_queryset(self):
        if self.request.GET.get("name"):
            return Dish.objects.filter(
                model__icontains=self.request.GET.get("name")).select_related("dish_type")
        return Dish.objects.all().select_related("dish_type")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_create.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("taxi:car-list")
    template_name = "kitchen/dish_update.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("taxi:car-list")
    template_name = "kitchen/dish_delete.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    template_name = "kitchen/cook_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = CookSearchForm
        return context

    def get_queryset(self):
        if self.request.GET.get("username"):
            return Cook.objects.filter(
                username__icontains=self.request.GET.get("username"))
        return Cook.objects.all()


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")
    template_name = "kitchen/cook_detail.html"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "kitchen/cook_create.html"


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy("taxi:driver-list")
    template_name = "kitchen/cook_update.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("")
    template_name = "kitchen/cook_delete.html"


@login_required
def toggle_assign_to_dish(request, pk):
    cook = Cook.objects.get(id=request.user.id)
    if (
        Dish.objects.get(id=pk) in cook.cars.all()
    ):  # probably could check if car exists
        cook.cars.remove(pk)
    else:
        cook.cars.add(pk)
    return HttpResponseRedirect(reverse_lazy("taxi:car-detail", args=[pk]))
