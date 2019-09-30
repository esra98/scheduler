from django.shortcuts import render
from schedule_planner.backend import course_time_1to50

def home_page(request):
   return render(request, 'home_page.html')


def search(request):
   if request.method == 'POST':
       list = request.POST.getlist('coursename')
       course_1 = list[0]
       course_2 = list[1]
       course_3 = list[2]
       course_4 = list[3]
       course_5 = list[4]
       course_6 = list[5]
       course_7 = list[6]
       days_selected = request.POST.getlist('weekday_select')
       days_selected1  = []

       if len(days_selected)==0:
           days_selected1 =[1,2,3,4,5]
       else:
           for element in days_selected:
               days_selected1.append(int(element))



       list = course_time_1to50.deneme_scheduler(course_1,course_2,course_3,course_4,course_5,course_6,course_7,days_selected1)
       if len(list)==0:
           return render(request, 'no_result.html')




       return render(request, 'result_page.html', {"list": list})