from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from users.models import Profile
from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image

from io import BytesIO
from .models import Passouts, Placement, Batches, Post
import csv

from .Mail import send
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def sendmail(request):
    send()
    return render(request, 'sendmail.html', {})

def showimage(request):
    # Construct the graph
    # df = pandas.read_csv("placement.csv")
    # print(df["Region", "End_Date"])
    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)
    plot(t, s, linewidth=1.0)

    xlabel('Region ')
    ylabel('End Date')
    title('Region Wise Analysis')
    grid(True)

    buffer = BytesIO()

    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes(
        "RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


class PostListView(ListView):
    is_hr = False
    is_operations = False
    is_accounts = False
    is_audit = False
    is_hod = False
    is_enc = False
    is_imapact = False

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        print(self.request.user.id)
        profile = Profile.objects.get(user=self.request.user)
        print(profile.is_accounts)
        context["is_hr"] = profile.is_hr
        context["is_operations"] = profile.is_operations
        context["is_accounts"] = profile.is_accounts
        context["is_audit"] = profile.is_audit
        context["is_hod"] = profile.is_hod
        context["is_enc"] = profile.is_enc
        context["is_imapact"] = profile.is_imapact

        data = Batches.objects.all()
        res = serializers.serialize('json', data)
        context["dataset"] = res
        # t = arange(0.0, 2.0, 0.01)
        # s = sin(2*pi*t)
        # plot(t, s, linewidth=1.0)

        # xlabel('time (s)')
        # ylabel('voltage (mV)')
        # title('About as simple as it gets, folks')
        # grid(True)

        # # Store image in a string buffer
        # buffer = StringIO.StringIO()
        # canvas = pylab.get_current_fig_manager().canvas
        # canvas.draw()
        # pilImage = PIL.Image.frombytes(
        #     "RGB", canvas.get_width_height(), canvas.tostring_rgb())
        # pilImage.save(buffer, "PNG")
        # pylab.close()
        # data = HttpResponse(buffer.getvalue(), content_type="image/png")
        # context["graphData"] = data
        print(res)
        return context

    dataReader = csv.reader(open(
        r'C:\\Users\\prakh\\Desktop\\J.P.Morgan\\CodeForGood\\team-58\\Sameeksha\\django_project\\blog\\passout.csv'), delimiter=',', quotechar='"')
    next(dataReader)
    for row in dataReader:
        passout = Passouts()
        passout.Region = row[0]
        passout.LCDM_Name = row[1]
        passout.LDC_Name = row[2]
        passout.Batch_Code = row[3]
        passout.Status = row[4]
        passout.Start_Date = row[5]
        passout.End_Date = row[6]
        passout.Course_Name = row[7]
        passout.Full_Name = row[8]
        passout.DOB = row[9]
        passout.save()

    dataReader = csv.reader(open(
        r'C:\\Users\\prakh\\Desktop\\J.P.Morgan\\CodeForGood\\team-58\\Sameeksha\\django_project\\blog\\placement.csv'), delimiter=',', quotechar='"')
    next(dataReader)
    for row in dataReader:
        placement = Placement()
        placement.Region = row[0]
        placement.ReporteeLDCM = row[1]
        placement.LDCM = row[2]
        placement.LDC_Name = row[3]
        placement.Batch_Code = row[4]
        placement.Course_Name = row[5]
        placement.Start_Date = row[6]
        placement.End_Date = row[7]
        placement.Student_Id = row[8]
        placement.Student_Name = row[9]
        placement.save()

    dataReader = csv.reader(open(
        r'C:\\Users\\prakh\\Desktop\\J.P.Morgan\\CodeForGood\\team-58\\Sameeksha\\django_project\\blog\\batches.csv'), delimiter=',', quotechar='"')
    next(dataReader)
    for row in dataReader:
        batches = Batches()
        batches.Region = row[0]
        batches.Center_Name = row[1]
        batches.LDCM_Name = row[2]
        batches.Reportee = row[3]
        batches.Batch_Type = row[4]
        batches.Batch_Code = row[5]
        batches.Course_Name = row[6]
        batches.Course_Name2 = row[7]
        batches.Status = row[8]
        batches.Start_Date = row[9]
        batches.save()

    # response = HttpResponse(data, content_type="text/json-comment-filtered")

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
