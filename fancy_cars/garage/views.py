from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, 
                                       UpdateView,
                                       DeleteView)
from .models import Car
from django.urls import reverse_lazy


class CarListView(ListView):
    model = Car

class CarDetailView(DetailView):
    model = Car

#Filter
class CarListViewByMake(ListView):
    model = Car
    template_name ="garage/car_make.html"

    def get_context_data(self, **kwargs): # Returns a dictionary
         context = super(CarListViewByMake,self).get_context_data(**kwargs)
        #instead of return use content can be coconut
         print("This is KWARGS", self.kwargs)
         print("what kind of object this is???", type(self.kwargs))
         print("These are the keys",list(self.kwargs.keys()))
         make = self.kwargs.get("make").capitalize()
         print("----->", make)
         car_list = Car.objects.filter(make__icontains=make)
        #  car_list = Car.objects.filter(make=make)# make is less case senitive
         print(car_list)
        #  print(context)
         context['sorted_by_make'] = car_list
         context["coconut"] = make
         return context #Superfunction binds
    
class CarListView(ListView):
    model = Car

    def get_context_data(self, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        distinct_list = Car.objects.all()
        print("List Make: ", distinct_list)        
        distinct_list_make = distinct_list.values("make").distinct()
        print("Distinct List Make: ", distinct_list_make)        
        context["menu_make"] = distinct_list_make
        distinct_list_color = distinct_list.values("color").distinct()
        print("Distinct List Color: ", distinct_list_color)
        context["menu_color"] = distinct_list_color
        print(context)
        return context
    
class CarListViewByColor(ListView):
    model = Car
    template_name ="garage/car_color.html"

    def get_context_data(self, **kwargs): # Returns a dictionary
         context = super(CarListViewByColor,self).get_context_data(**kwargs)
        #instead of return use content can be coconut
         print("This is KWARGS", self.kwargs)
         print("what kind of object this is???", type(self.kwargs))
         print("These are the keys",list(self.kwargs.keys()))
         color = self.kwargs.get("color").capitalize()
         print("----->", color)
         car_list = Car.objects.filter(color__icontains=color)
        #  car_list = Car.objects.filter(make=make)# make is less case senitive
         print(car_list)
        #  print(context)
         context['sorted_by_color'] = car_list
         context["color"] = color
         print("Type of content: ", type(context))
         print("Car List: ", car_list)
         print("Content: ", context)
         return context #Superfunction binds
         
class CarCreateView(CreateView):
        model = Car
        fields = [
            "make",
            "model",
            "color",
            "image",
            "horsepower"
            
        ]
        success_url = reverse_lazy("car-list")

class CarUpdateView(UpdateView):
    model = Car
    fields = [
        "make",
        "model",
        "color",
        "image",
        "horsepower",
    ]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('car-list')

class CarDeleteView(DeleteView):
     model = Car
     success_url = reverse_lazy('car-list')