from django.shortcuts import render, HttpResponse, redirect
from bloghome.forms import *
from bloghome.models import *


# Create your views here.
def landing_page(request):
    context = {"dataset1": BlogPostOne.objects.all(),
               "dataset2": BlogPostTwo.objects.all(),
               "dataset3": BlogPostThree.objects.all(),
               "dataset4": BlogPostFour.objects.all(),
               "dataset5": BlogPostFive.objects.all(),
               "dataset6": BlogPostSix.objects.all(),
               "dataset7": BlogPostSeven.objects.all(),
               "dataset8": BlogPostEight.objects.all(),
               "dataset9": BlogPostNine.objects.all()}
    return render(request, 'dashboard.html', context)


def page_1(request):
    context = {"dataset": BlogPostOne.objects.all()}
    return render(request, 'blog_page.html', context)


def page_2(request):
    context = {"dataset": BlogPostTwo.objects.all()}
    return render(request, 'blog_page.html', context)


def page_3(request):
    context = {"dataset": BlogPostThree.objects.all()}
    return render(request, 'blog_page.html', context)


def page_4(request):
    context = {"dataset": BlogPostFour.objects.all()}
    return render(request, 'blog_page.html', context)


def page_5(request):
    context = {"dataset": BlogPostFive.objects.all()}
    return render(request, 'blog_page.html', context)


def page_6(request):
    context = {"dataset": BlogPostSix.objects.all()}
    return render(request, 'blog_page.html', context)


def page_7(request):
    context = {"dataset": BlogPostSeven.objects.all()}
    return render(request, 'blog_page.html', context)


def page_8(request):
    context = {"dataset": BlogPostEight.objects.all()}
    return render(request, 'blog_page.html', context)


def page_9(request):
    context = {"dataset": BlogPostNine.objects.all()}
    return render(request, 'blog_page.html', context)


def success_upld(request):
    return HttpResponse('successfully uploaded')


def success_dlt(request):
    return HttpResponse('successfully deleted')


def blogPostUpdate(request):
    if request.method == 'POST' and 'btnform1' in request.POST:
        form1 = BlogUpdateFormOne(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('success_upld')
    else:
        form1 = BlogUpdateFormOne()
    if request.method == 'POST' and 'btnform2' in request.POST:
        form2 = BlogUpdateFormTwo(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('success')
    else:
        form2 = BlogUpdateFormTwo()
    if request.method == 'POST' and 'btnform3' in request.POST:
        form3 = BlogUpdateFormThree(request.POST, request.FILES)
        if form3.is_valid():
            form3.save()
            return redirect('success')
    else:
        form3 = BlogUpdateFormThree()
    if request.method == 'POST' and 'btnform4' in request.POST:
        form4 = BlogUpdateFormFour(request.POST, request.FILES)
        if form4.is_valid():
            form4.save()
            return redirect('success_upld')
    else:
        form4 = BlogUpdateFormFour()
    if request.method == 'POST' and 'btnform5' in request.POST:
        form5 = BlogUpdateFormFive(request.POST, request.FILES)
        if form5.is_valid():
            form5.save()
            return redirect('success_upld')
    else:
        form5 = BlogUpdateFormFive()
    if request.method == 'POST' and 'btnform5' in request.POST:
        form6 = BlogUpdateFormSix(request.POST, request.FILES)
        if form6.is_valid():
            form6.save()
            return redirect('success_upld')
    else:
        form6 = BlogUpdateFormSix()
    if request.method == 'POST' and 'btnform7' in request.POST:
        form7 = BlogUpdateFormSeven(request.POST, request.FILES)
        if form7.is_valid():
            form7.save()
            return redirect('success_upld')
    else:
        form7 = BlogUpdateFormSeven()
    if request.method == 'POST' and 'btnform8' in request.POST:
        form8 = BlogUpdateFormEight(request.POST, request.FILES)
        if form8.is_valid():
            form8.save()
            return redirect('success_upld')
    else:
        form8 = BlogUpdateFormEight()
    if request.method == 'POST' and 'btnform9' in request.POST:
        form9 = BlogUpdateFormNine(request.POST, request.FILES)
        if form9.is_valid():
            form9.save()
            return redirect('success_upld')
    else:
        form9 = BlogUpdateFormNine()

    return render(request, 'form.html', {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4,
                                         'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8,
                                         'form9': form9})


def delete_view(request, id):
    if id == '1':
        BlogPostOne.objects.all().delete()
    if id == '2':
        BlogPostTwo.objects.all().delete()
    if id == '3':
        BlogPostThree.objects.all().delete()
    if id == '4':
        BlogPostFour.objects.all().delete()
    if id == '5':
        BlogPostFive.objects.all().delete()
    if id == '6':
        BlogPostSix.objects.all().delete()
    if id == '7':
        BlogPostSeven.objects.all().delete()
    if id == '8':
        BlogPostEight.objects.all().delete()
    if id == '9':
        BlogPostNine.objects.all().delete()

    return redirect('success_dlt')
