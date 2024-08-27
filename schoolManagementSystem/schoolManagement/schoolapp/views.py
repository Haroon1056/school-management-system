from django.shortcuts import render, redirect
from .models import Student, Result, Fee
from .forms import StudentForm, ResultForm, FeeForm


def index(request):
    return render(request, "index.html")

def create_student(request):
    form = StudentForm
    return render(request, "create_student.html", {'form': form})

def add_student(request):
    form = StudentForm(request.POST)
    form.save()
    return redirect('/student_list')
    
def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {'students': students})    

def edit_student(request, id):
    students = Student.objects.get(id=id)
    return render(request, "edit_student.html", {'students': students})

def update_student(request, id):
    students = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=students)
    form.save()
    return redirect('/student_list')

def delete_student(request, id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect('/student_list')

def search_student(request):
    given_name = request.POST['name']             #when i use ename there use many function like only ename, ename__iexact (not case sensetive) and ename__icontains (search minimun two letters)
    students = Student.objects.filter(first_name__icontains=given_name)
    return render(request, "student_list.html", {'students': students})
    
#Result Part

def create_result(request):
    form = ResultForm
    return render(request, "create_result.html", {'form': form})

def add_result(request):
    form = ResultForm(request.POST)
    form.save()
    return redirect('/result_list')

def result_list(request):
    results = Result.objects.all()
    return render(request, "result_list.html", {'results': results})    


def delete_result(request, id):
    results = Result.objects.get(id=id)
    results.delete()
    return redirect('/result_list')

def search_result(request):
    given_name = request.POST['name']             #when i use ename there use many function like only ename, ename__iexact (not case sensetive) and ename__icontains (search minimun two letters)
    results = Result.objects.filter(marks__icontains=given_name)
    return render(request, "result_list.html", {'results': results})


# Fee part

def create_fee(request):
    form = FeeForm
    return render(request, "create_fee.html", {'form': form})

def add_fee(request):
    form = FeeForm(request.POST)
    form.save()
    return redirect('/fee_list')
    
def fee_list(request):
    fees = Fee.objects.all()
    return render(request, "fee_list.html", {'fees': fees})    


def delete_fee(request, id):
    fees = Fee.objects.get(id=id)
    fees.delete()
    return redirect('/fee_list')

def search_fee(request):
    given_name = request.POST['name']             #when i use ename there use many function like only ename, ename__iexact (not case sensetive) and ename__icontains (search minimun two letters)
    fees = Fee.objects.filter(amount__icontains=given_name)
    return render(request, "fee_list.html", {'fees': fees})
# Create your views here.
