from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic import View
import json
from studentapp.utils import valid_json
from studentapp.models import Student
from studentapp.mixins import HttpResponseMixin, SerializeMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from studentapp.forms import StudentForm

@method_decorator(csrf_exempt,name='dispatch')
class StudentCBV(HttpResponseMixin,SerializeMixin,View):
    #This is utility method can be called by POST, GET, PUT, DELETE
    def get_object_by_id(self,id):
        try:
            s = Student.objects.get(id=id)
        except Student.DoesNotExist:
            s = None
        return s
    #This is general method to get all data with some condition and JSON validation
    def get(self,request,*args,**kwargs):
        data = request.body
        if not valid_json:                                                  #Sent for json validation
            data={'msg':'Please send valid json file'}
            return self.render_me(json.dumps(data), status=400)             #send for rendering in mixin
        data = json.loads(data)
        p_data = data.get('id',None)
        if p_data is not None:                                              #check if data is Present or not
            std_data = self.get_object_by_id(p_data)
            if std_data is None:
                data={'msg':'No matched record found with this id'}
                return self.render_me(json.dumps(data), status=400)
            json_data = self.serialize_me([std_data])                       #single object serializing using list
            return self.render_me(json_data)
        std_data = Student.objects.all()
        json_data = self.serialize_me(std_data)                             #sending query for serializing
        return self.render_me(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        if not valid_json:
            data={'msg':'Please send valid json file'}
            return self.render_me(json.dumps(data), status=400)
        std_data = json.loads(data)
        form = StudentForm(std_data)
        if form.is_valid():                                                 #form checking with forms module
            form.save(commit=True)
            data={'msg':'Resource created successfully!'}
            return self.render_me(json.dumps(data))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_me(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data = request.body
        if not valid_json:
            data={'msg':'Please send valid json file'}
            return self.render_me(json.dumps(data), status=400)
        new_data = json.loads(data)
        p_data = new_data.get('id',None)
        if p_data is None:                                                  #check if data is Present or not
            data={'msg':'id is mandatory to perform updation'}
            return self.render_me(json.dumps(data), status=400)
        std = self.get_object_by_id(p_data)
        if std is None:
            data = ({'msg':'No mathched record found with given id'})
            return self.render_me(json.dumps(data),status=400)
        original_data = {
            'name': std.name,
            'rollno': std.rollno,
            'marks': std.marks,
            'teacher': std.teacher,
            'f_subject':std.f_subject,
        }
        original_data.update(new_data)
        form = StudentForm(original_data,instance=std)                       #take same object as recived
        if form.is_valid():                                                 #form checking with forms module
            form.save(commit=True)
            data={'msg':'Resource Updated successfully!'}
            return self.render_me(json.dumps(data))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_me(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data = request.body
        if not valid_json:
            data={'msg':'Please send valid json file'}
            return self.render_me(json.dumps(data), status=400)
        new_data = json.loads(data)
        p_data = new_data.get('id',None)
        if p_data is None:                                                  #check if data is Present or not
            data={'msg':'id is mandatory to perform deletion'}
            return self.render_me(json.dumps(data), status=400)
        std = self.get_object_by_id(p_data)
        if std is None:
            data = ({'msg':'No mathched record found with given id not possible to delete'})
            return self.render_me(json.dumps(data),status=400)
        status,deleted_item = std.delete()
        if status == 1:
            json_data = json.dumps({'msg':'Resource deleted successfully!'})
            return self.render_me(json_data)
        json_data = json.dumps({'msg':'unable to delete.. please try again!'})
        return self.render_me(json_data,status=500)
