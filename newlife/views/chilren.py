# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.forms import ModelForm
from django.views.generic import UpdateView, CreateView, DeleteView

from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Field

from ..models import Child, Group
from ..util import paginate

# Create your views here.
# Views for students
def children_list(request):
	children = Child.objects.all()
	
	#ordering students 
	order_by=request.GET.get('order_by','')
	children=children.order_by('last_name')
	if request.GET.get('order_by', '') == '':
		request.GET.order_by = 'last_name'
	#order_by = request.GET.get('order_by', '')
	
	if order_by in ('last_name','first_name','id'):
		children=children.order_by(order_by)
		if request.GET.get('reverse','')=='1':
			children=children.reverse()
	
	# #paginate students
	# paginator = Paginator(students, 6)
	# page = request.GET.get('page')
	# try:
	# 	students = paginator.page(page)
	# except PageNotAnInteger:
	# 	# If page is not an integer, deliver first page.
	# 	students = paginator.page(1)
	# except EmptyPage:
	# 	# If page is out of range (e.g. 9999), deliver last page of results.
	
	context = paginate(children, 8, request,{}, var_name = 'children')

	return render(request, 'newlife/children_list.html', context)


class StudentCreateForm(ModelForm):
	class Meta:
		model = Student
		fields = "__all__"

	def __init__(self, *args, **kwargs):
    	    super(StudentCreateForm, self).__init__(*args, **kwargs)
    
	    self.helper=FormHelper(self)

    	    self.helper.form_action = reverse('students_add')

    	    self.helper.form_class = 'form-horizontal'
    	    self.helper.form_mehtod = 'POST'

        #twitter bootstrap styles

    	    self.helper.help_text_inline = True
    	    self.helper.html5_required = True
    	    self.helper.label_class = 'col-sm-2 control-label'
    	    self.helper.field_class = 'col-sm-10'

    	    self.fields['birthday'].widget.attrs['placeholder'] = u'Напр. 1988-11-29' 

    	    break_message= u"Додавання студента відмінено"
    	    self.helper.layout[-1]= Layout(
    	    	Field('notes',css_class='input-xlarge',),
    	    	FormActions(
            Submit('add_button',u'Зберегти', css_class="btn btn-priamry"),
            HTML("<a class='btn btn-link' id = 'cancel-id-send_button' href='{% url 'home' %}?status_message="+break_message+"' name = 'cancel_button'>"+u'Скасувати'+"</a>"),
            ))



class StudentCreateView(CreateView):
	model = Student
	template_name = "students/students_universal.html"
	form_class = StudentCreateForm

	def get_success_url(self):
		return u'%s?status_message=Студента успішно збережено!'%reverse('home')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Створення студента відмінено'%reverse('home'))
		else:
			return super(StudentCreateView, self).post(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context["name"] = 'Додати'

		return context

	





# def students_add(request):
# 	storage = get_messages(request) # removing old messages
# 	for message in storage:
# 		pass


	# # If form was posted
	# if request.method == "POST":
	# 	# was form add_button clicked
	# 	if request.POST.get('add_button') is not None:

	# 		data = {'middle_name':request.POST.get('middle_name'),'notes':request.POST.get('notes')}
	# 		#TODO: validate input errors from user
	# 		errors ={}

	# 		first_name=request.POST.get('first_name','').strip()
	# 		if not first_name:
	# 			errors['first_name'] = u"Ім'я є обов'язковим"
	# 		else:
	# 			data['first_name']=first_name 

	# 		last_name=request.POST.get('last_name','').strip()
	# 		if not last_name:
	# 			errors['last_name'] = u"Прізвище є обов'язковим"
	# 		else:
	# 			data['last_name']=last_name

	# 		birthday=request.POST.get('birthday','').strip()
	# 		if not birthday:
	# 			errors['birthday'] = u"Дата народження є обов'язковою"
	# 		else:
	# 			try:
	# 				datetime.strptime(birthday,'%Y-%m-%d')
	# 			except Exception:
	# 				errors['birthday']=u"Введіть коректну дату(напр. 1984-12-30)"

	# 			else:
	# 				data['birthday']=birthday

	# 		ticket=request.POST.get('ticket','').strip()
	# 		if not ticket:
	# 			errors['ticket'] = u"Номер білета є обов'язковим"
	# 		else:
	# 			data['ticket']=ticket

	# 		student_group=request.POST.get('student_group','').strip()
	# 		if not student_group:
	# 			errors['student_group'] = u"Група є обов'язкова"
	# 		else:
	# 			groups=Group.objects.filter(pk=student_group)
	# 			if len(groups)!=1:
	# 				errors['student_group']=u"Оберіть коректну групу"
	# 			else:
	# 				data['student_group']=groups[0]

	# 		formats = ['jpg','jpeg','bmp','png','gif','riff']

	# 		photo=request.FILES.get('photo')
	# 		if photo:
	# 			file_name = photo.name.split('.')
	# 			if photo.size > 2000000:
	# 				errors['photo'] = u"Розмір файлу завеликий"
	# 			elif file_name[1] not in formats:
	# 				errors['photo'] = u"Це має бути фото"
	# 			else:
	# 				data['photo']=photo

			

	# 		if not errors:
	# 			#create student
	# 			student=Student(**data)
	# 			#save student to database
	# 			student.save()

	# 			#redirect user to the students list

	# 			return HttpResponseRedirect(u'%s?status_message=Студента %s %s успішно додано'%(reverse('home'), data['first_name'], data['last_name']))

	# 		else:
	# 			# render form with errors and previous user input
	# 			for error_name in errors:
	# 				messages.add_message(request,messages.INFO, errors[error_name])
	# 			return render(request, 'students/students_add.html',{'groups':Group.objects.all().order_by('title'),
	# 				'errors':errors})
	# 	elif request.POST.get('cancel_button') is not None:
	# 		#redirect to homepage

	# 		return HttpResponseRedirect(u'%s?status_message=Додавання студента відмінено'%reverse('home'))
	# else:
	# 	#initial form render
	# 	return render(request,'students/students_add.html',{'groups':Group.objects.all().order_by('title')})

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper=FormHelper(self)

        self.helper.form_action = reverse('students_edit', kwargs={'pk':kwargs['instance'].id})

        self.helper.form_class = 'form-horizontal'
        self.helper.form_mehtod = 'POST'

        #twitter bootstrap styles

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout[-1]= Layout(
    	    	Field('notes',css_class='input-xlarge'),
    	    	FormActions(
            Submit('add_button',u'Зберегти', css_class="btn btn-priamry"),
            Submit('cancel_button',u'Скасувати', css_class="btn btn-link"),
            ))


class StudentUpdateView(UpdateView):
	model = Student
	template_name="students/students_universal.html"
	form_class=StudentUpdateForm

	def get_success_url(self):
		return u'%s?status_message=Студента успішно збережено!'%reverse('home')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено!'%reverse('home'))
		else:
			return super(StudentUpdateView, self).post(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context["name"] = 'Редагувати'

		return context
	

class StudentDeleteView(DeleteView):
	model = Student
	template_name  = "students/students_confirm_delete.html"

	def get_success_url(self):
		return u'%s?status_message=Студента успішно видалено!'%reverse('home')

def students_delete(request, sid):
    if request.method == 'POST':
        if "delete_button" in request.POST:
            student = Student.objects.get(id  = sid )
            student.delete()
            return HttpResponseRedirect(u'%s?status_message=Студента успішно видалено'%reverse('home'))
        elif "cancel_button" in request.POST:
            return HttpResponseRedirect(u'%s?status_message=Видалення студента відмінено'%reverse('home'))
    else:
        return render(request, 'students/students_confirm_delete.html',{'object':Student.objects.get(id  = sid )})

def students_delete_several(request):
    students = Student.objects.all()
    

    if request.GET.get('delete_button1') is not None:
        students_id = request.GET.getlist('chosen')
        studenttodelete=Student.objects.filter(pk__in = students_id)

        return render(request, 'students/students_confirm_delete_several.html', {'objects':studenttodelete, 'ids':students_id})

   

    if request.method =='POST':
        if "delete_button" in request.POST:
            students_id = request.POST.getlist('ids')
            studenttodelete=Student.objects.filter(pk__in = students_id).delete()
            return HttpResponseRedirect(u'%s?status_message=Студенти успішно видалені'%reverse('home'))
        elif "cancel_button" in request.POST:
            return HttpResponseRedirect(u'%s?status_message=Видалення студентів відмінено'%reverse('home'))
    else: 
        return render(request, 'students/students_delete_several.html',{'students':students})

    return render(request, 'students/students_delete_several.html',{'students':students})
