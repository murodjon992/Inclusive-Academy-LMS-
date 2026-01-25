from django.contrib import messages
from .forms import RegistrationForm, LoginForm, AdminUserCreateForm,AmaliyotTuriForm,NewsForm,SahifaRasmiForm,CourseForm,QuestionForm,QuizForm,CourseModuleForm,LessonForm,CourseEnrollmentForm,AnswerForm,KutubxonaCategoryForm,KutubxonaItemForm,AmaliyotItemForm,AmaliyotVideoForm,AmaliyotSectionForm,RelatedPracticeForm,CustomUserForm
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import  Question,CustomUser,Certificate,AmaliyotTuri,News,SahifaRasmi,QuizResult,CourseTest,Course,CourseModule,CourseEnrollment,KutubxonaItem,KutubxonaCategory,Lesson,LessonProgress,Answer,AmaliyotItem,AmaliyotSection,AmaliyotVideo,RelatedPractice
from django.http import JsonResponse,HttpResponseNotAllowed,FileResponse
from django.utils import timezone
import mimetypes
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# =============================== COURSE ==========================
def admin_add_course(request,course_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if course_id:
        course = get_object_or_404(Course, id=course_id)
    else:
        course = None
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_course')
    else:
        form = CourseForm(instance=course)
        kurslar = Course.objects.all()
    return render(request, 'admin/add-course.html', {'form': form, 'kurslar': kurslar,'course': course})

def admin_delete_course(request,course_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('inclusive_app:admin_add_course')
# ================== COURSE END ==========================

# =====================COURSE MODULE==========================
def admin_add_coursemodule(request,coursemodule_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if coursemodule_id:
        coursemodule = get_object_or_404(CourseModule, id=coursemodule_id)
    else:
        coursemodule = None
    if request.method == "POST":
        form = CourseModuleForm(request.POST, request.FILES, instance=coursemodule)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_coursemodule')
    else:
        form = CourseModuleForm(instance=coursemodule)
        kursmodullar = CourseModule.objects.all()
    return render(request, 'admin/add-coursemodule.html', {'form': form, 'kursmodullar': kursmodullar,'coursemodule': coursemodule})

def admin_delete_coursemodule(request,coursemodule_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    coursemodule = get_object_or_404(Course, id=coursemodule_id)
    coursemodule.delete()
    return redirect('inclusive_app:admin_add_coursemodule')
# ================== COURSE MODULE END ==========================

# =============================== TEST ==========================
def admin_add_coursetest(request,coursetest_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if coursetest_id:
        coursetest = get_object_or_404(CourseTest, id=coursetest_id)
    else:
        coursetest = None
    if request.method == "POST":
        form = QuizForm(request.POST, instance=coursetest)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_coursetest')
    else:
        form = QuizForm(instance=coursetest)
        testlar = CourseTest.objects.all()
    return render(request, 'admin/add-test.html', {'form': form, 'testlar': testlar,'coursetest': coursetest})

def admin_delete_coursetest(request,coursetest_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    coursetest = get_object_or_404(CourseTest, id=coursetest_id)
    coursetest.delete()
    return redirect('inclusive_app:admin_add_coursetest')
# ================== TEST END ==========================

# =============================== Lesson ==========================
def admin_add_lesson(request,lesson_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if lesson_id:
        lesson = get_object_or_404(Lesson, id=lesson_id)
    else:
        lesson = None
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_lesson')
    else:
        form = LessonForm(instance=lesson)
        darslar = Lesson.objects.all()
    return render(request, 'admin/add-lesson.html', {'form': form, 'darslar': darslar,'lesson': lesson})

def admin_delete_lesson(request,lesson_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    lesson = get_object_or_404(CourseTest, id=lesson_id)
    lesson.delete()
    return redirect('inclusive_app:admin_add_lesson')
# ================== LESSON END ==========================

# =================== COURSE ENROLLEMENT ==========================
def admin_add_courseenrollement(request,courseenroll_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if courseenroll_id:
        courseenroll = get_object_or_404(CourseEnrollment, id=courseenroll_id)
    else:
        courseenroll = None
    if request.method == "POST":
        form = CourseEnrollmentForm(request.POST, request.FILES, instance=courseenroll)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_courseenrollement')
    else:
        form = CourseEnrollmentForm(instance=courseenroll)
        kursenrollar = CourseEnrollment.objects.all()
    return render(request, 'admin/courseenroll.html', {'form': form, 'kursenrollar': kursenrollar,'courseenroll': courseenroll})

def admin_delete_courseenrollement(request,courseenroll_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    courseenroll = get_object_or_404(CourseEnrollment, id=courseenroll_id)
    courseenroll.delete()
    return redirect('inclusive_app:admin_add_courseenrollement')
# ================== COURSE ENROLLEMENT END ==========================

# ================== COURSE PROGRESS ==========================
def admin_course_progress(request):
    enrollments = CourseEnrollment.objects.select_related('user', 'course')

    data = []
    for e in enrollments:
        total = Lesson.objects.filter(
            module__course=e.course
        ).count()

        completed = LessonProgress.objects.filter(
            enrollment=e,
            is_completed=True
        ).count()

        progress = int((completed / total) * 100) if total > 0 else 0
        quiz_unlocked = progress == 100

        data.append({
            'user': e.user,
            'course': e.course,
            'completed': completed,
            'total': total,
            'progress': progress,
            'quiz_unlocked': quiz_unlocked,
        })

    return render(
        request,
        'admin/lesson-progress.html',
        {'data': data}
    )
# ================== COURSE PROGRESS END ==========================

# =================== SAVOLLAR ==========================
def admin_add_question(request,question_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if question_id:
        question = get_object_or_404(Question, id=question_id)
    else:
        question = None
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_question')
    else:
        form = QuestionForm(instance=question)
        savollar = Question.objects.all()
    return render(request, 'admin/add-questions.html', {'form': form, 'savollar': savollar,'question': question})

def admin_delete_question(request,question_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return redirect('inclusive_app:admin_add_course')
# ================== SAVOLLAR END ==========================


# =================== JAVOBLAR ==========================
def admin_add_variable(request,variable_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if variable_id:
        variable = get_object_or_404(Answer, id=variable_id)
    else:
        variable = None
    javoblar = Answer.objects.all()
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=variable)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_variable')
    else:
        form = AnswerForm(instance=variable)
    return render(request, 'admin/add-variable.html', {'form': form, 'javoblar': javoblar,'variable': variable})

def admin_delete_variable(request,variable_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    variable = get_object_or_404(Answer, id=variable_id)
    variable.delete()
    return redirect('inclusive_app:admin_add_variable')
# ================== JAVOB END ==========================

# =================== YANGILIKLAR ==========================
def admin_add_yangiliklar(request,yangilik_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if yangilik_id:
        variable = get_object_or_404(News, id=yangilik_id)
    else:
        yangilik = None

    yangiliklar = News.objects.all()

    if request.method == "POST":
        form = NewsForm(request.POST, instance=yangilik)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_yangiliklar')
    else:
        form = NewsForm(instance=yangilik)
    return render(request, 'admin/add-yangiliklar.html', {'form': form, 'yangiliklar': yangiliklar,'yangilik': yangilik})

def admin_delete_yangiliklar(request,yangilik_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    yangilik = get_object_or_404(News, id=yangilik_id)
    yangilik.delete()
    return redirect('inclusive_app:admin_add_yangiliklar')
# ================== YANGILIKLAR END ==========================

# =================== SAHIFA RASMLARI ==========================
def admin_add_sahifarasm(request,sahifarasm_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if sahifarasm_id:
        sahifarasm = get_object_or_404(News, id=sahifarasm_id)
    else:
        sahifarasm = None

    if request.method == "POST":
        form = SahifaRasmiForm(request.POST, request.FILES, instance=sahifarasm)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_sahifarasm')
    else:
        form = SahifaRasmiForm(instance=sahifarasm)
    sahifarasmlar = SahifaRasmi.objects.all()
    return render(request, 'admin/add-sahifarasm.html', {'form': form, 'sahifarasmlar': sahifarasmlar,'sahifarasm': sahifarasm})

def admin_delete_sahifarasm(request,sahifarasm_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    sahifarasm = get_object_or_404(SahifaRasmi, id=sahifarasm_id)
    sahifarasm.delete()
    return redirect('inclusive_app:admin_add_sahifarasm')
# ================== SAHIFA RASMLARI END ==========================

# =================== KUTUBXONA BO'LIMI ==========================
def admin_add_catkutubxona(request,catkutubxona_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if catkutubxona_id:
        catkutubxona = get_object_or_404(KutubxonaCategory, id=catkutubxona_id)
    else:
        catkutubxona = None

    if request.method == "POST":
        form = KutubxonaCategoryForm(request.POST, request.FILES, instance=catkutubxona)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_catkutubxona')
    else:
        form = KutubxonaCategoryForm(instance=catkutubxona)
    bolimlar = KutubxonaCategory.objects.all()
    return render(request, 'admin/add-kutubxonacategoriya.html', {'form': form, 'bolimlar': bolimlar,'catkutubxona': catkutubxona})

def admin_delete_catkutubxona(request,catkutubxona_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    catkutubxona = get_object_or_404(KutubxonaCategory, id=catkutubxona_id)
    catkutubxona.delete()
    return redirect('inclusive_app:admin_add_catkutubxona')
# ================== KUTUBXONA BO'LIMI END ==========================

# =================== KUTUBXONA MANBALAR ==========================
def admin_add_mankutubxona(request,mankutubxona_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if mankutubxona_id:
        mankutubxona = get_object_or_404(KutubxonaItem, id=mankutubxona_id)
    else:
        mankutubxona = None

    if request.method == "POST":
        form = KutubxonaItemForm(request.POST, request.FILES, instance=mankutubxona)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_mankutubxona')
    else:
        form = KutubxonaItemForm(instance=mankutubxona)
    manbalar = KutubxonaItem.objects.all()
    return render(request, 'admin/add-kutubxonamanba.html', {'form': form, 'manbalar': manbalar,'mankutubxona': mankutubxona})

def admin_delete_mankutubxona(request,mankutubxona_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    mankutubxona = get_object_or_404(KutubxonaItem, id=mankutubxona_id)
    mankutubxona.delete()
    return redirect('inclusive_app:admin_add_mankutubxona')
# ================== KUTUBXONA MANBALAR END ==========================
@login_required
def admin_certificate_list(request):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    results = request.user.test_results.all()
    sertifikatlar = Certificate.objects.select_related('user', 'test_result')
    return render(request,'admin/sertifikatlar.html', {'sertifikatlar': sertifikatlar,'results': results})


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    users = CustomUser.objects.all().count()
    certificates = Certificate.objects.all().count()
    return render(request, "admin/index.html",{'users': users,'certificates': certificates})


@login_required
def admin_add_user(request,user_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if user_id:
        user = get_object_or_404(CustomUser, id=user_id)
    else:
        user = None
    if request.method == "POST":
        form = AdminUserCreateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_user')
    else:
        form = AdminUserCreateForm(instance=user)
        users = CustomUser.objects.all().prefetch_related('test_results')
        foydalanuvchi = request.user
        results = foydalanuvchi.test_results.select_related('quiz').all()
    return render(request, "admin/user_list.html",{'users': users,'form': form,'user': user,'results': results})

def admin_delete_user(request,user_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('inclusive_app:admin_add_user')
# ================== AMALIYOTLAR ==========================
def admin_add_amaliyot(request,amaliyot_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if amaliyot_id:
        amaliyot = get_object_or_404(AmaliyotTuri, id=amaliyot_id)
    else:
        amaliyot = None
    if request.method == "POST":
        form = AmaliyotTuriForm(request.POST,instance=amaliyot)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_amaliyot')
    else:
        form = AmaliyotTuriForm(instance=amaliyot)
        amaliyotlar = AmaliyotTuri.objects.all()
    return render(request, 'admin/add-amaliyot.html', {'form': form, 'amaliyotlar': amaliyotlar,'amaliyot': amaliyot})

def admin_delete_amaliyot(request,amaliyot_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    amaliyot = get_object_or_404(AmaliyotTuri, id=amaliyot_id)
    amaliyot.delete()
    return redirect('inclusive_app:admin_add_amaliyot')
# ================== AMALIYOTLAR END ======================
# ================== AMALIYOT ITEMLAR ==========================
def admin_add_amaliyotitem(request,amaliyotitem_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if amaliyotitem_id:
        amaliyotitem = get_object_or_404(AmaliyotItem, id=amaliyotitem_id)
    else:
        amaliyotitem = None
    if request.method == "POST":
        form = AmaliyotItemForm(request.POST, request.FILES, instance=amaliyotitem)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_amaliyotitem')
    else:
        form = AmaliyotItemForm(instance=amaliyotitem)
        amaliyotItemlar = AmaliyotItem.objects.all()
    return render(request, 'admin/add-amaliyotitem.html', {'form': form, 'amaliyotItemlar': amaliyotItemlar,'amaliyotitem': amaliyotitem})

def admin_delete_amaliyotitem(request,amaliyotitem_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    amaliyotitem = get_object_or_404(AmaliyotItem, id=amaliyotitem_id)
    amaliyotitem.delete()
    return redirect('inclusive_app:admin_add_amaliyotitem')
# ================== AMALIYOT ITEMLAR END ======================
# ================== AMALIYOT RELATED ITEMLAR ==========================
def admin_add_relatedamaliyot(request,relamal_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")

    if relamal_id:
        relamal = get_object_or_404(RelatedPractice, id=relamal_id)
    else:
        relamal = None

    if request.method == "POST":
        form = RelatedPracticeForm(request.POST, instance=relamal)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_relatedamaliyot')
    else:
        form = RelatedPracticeForm(instance=relamal)
    items = RelatedPractice.objects.select_related(
            'from_item', 'to_item'
        )
    return render(request, 'admin/relatedamaliyot.html', {'form': form,'items': items})


def admin_delete_relatedamaliyot(request,relamal_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    relamal = get_object_or_404(RelatedPractice, id=relamal_id)
    relamal.delete()
    return redirect('inclusive_app:admin_add_relatedamaliyot')

# ================== AMALIYOT RELATED ITEMLAR END ======================
# ================== AMALIYOT VIDEOLAR ==========================
def admin_add_amaliyotvideo(request,amaliyotvideo_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if amaliyotvideo_id:
        amaliyotvideo = get_object_or_404(AmaliyotVideo, id=amaliyotvideo_id)
    else:
        amaliyotvideo = None
    if request.method == "POST":
        form = AmaliyotVideoForm(request.POST, request.FILES, instance=amaliyotvideo)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_amaliyotvideo')
    else:
        form = AmaliyotVideoForm(instance=amaliyotvideo)
        amaliyotVideolar = AmaliyotVideo.objects.all()
    return render(request, 'admin/add-amaliyotvideo.html', {'form': form, 'amaliyotVideolar': amaliyotVideolar,'amaliyotvideo': amaliyotvideo})

def admin_delete_amaliyotvideo(request,amaliyotvideo_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    amaliyotvideo = get_object_or_404(AmaliyotVideo, id=amaliyotvideo_id)
    amaliyotvideo.delete()
    return redirect('inclusive_app:admin_add_amaliyotvideo')
# ================== AMALIYOT VIDEOLAR END ======================
# ================== AMALIYOT SECTIONLAR ==========================
def admin_add_amaliyotsection(request,amaliyotsection_id=None):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    if amaliyotsection_id:
        amaliyotsection = get_object_or_404(AmaliyotSection, id=amaliyotsection_id)
    else:
        amaliyotsection = None
    if request.method == "POST":
        form = AmaliyotSectionForm(request.POST, request.FILES, instance=amaliyotsection)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:admin_add_amaliyotsection')
    else:
        form = AmaliyotSectionForm(instance=amaliyotsection)
        amaliyotSectionlar = AmaliyotSection.objects.all()
    return render(request, 'admin/add-amaliyotsection.html', {'form': form, 'amaliyotSectionlar': amaliyotSectionlar,'amaliyotsection': amaliyotsection})

def admin_delete_amaliyotsection(request,amaliyotsection_id):
    if not request.user.is_superuser:
        return redirect("inclusive_app:login_user")
    amaliyotsection = get_object_or_404(AmaliyotSection, id=amaliyotsection_id)
    amaliyotsection.delete()
    return redirect('inclusive_app:admin_add_amaliyotsection')
# ================== AMALIYOT SECTIONLAR END ======================
# User Views
def index(request):
    amaliyotlar = AmaliyotTuri.objects.all()
    yangiliklar = News.objects.all()
    darslar = Course.objects.prefetch_related('modules__lessons')
    bannerlar = SahifaRasmi.objects.filter(is_published=True).order_by('-created_at')[:3]
    return render(request, 'pages/index.html', {'amaliyotlar': amaliyotlar,'yangiliklar': yangiliklar,'bannerlar': bannerlar, 'darslar': darslar})

def yangilik_detail(request,slug):
    yangilik = get_object_or_404(News, slug=slug,is_published=True)
    return render(request, 'pages/yangilik-detail.html', {'yangilik': yangilik})

def amaliyot_items(request, slug):
    tur = get_object_or_404(AmaliyotTuri, slug=slug)
    items = tur.items.all().order_by('-created_at')

    return render(request, 'pages/oqitish-amaliyoti.html', {
        'tur': tur,
        'items': items
    })

def amaliyot_item_detail(request, tur_slug, item_slug):
    tur = get_object_or_404(AmaliyotTuri, slug=tur_slug)
    item = get_object_or_404(
        AmaliyotItem,
        slug=item_slug,
        turi=tur
    )

    related_items = RelatedPractice.objects.filter(
        from_item=item
    ).select_related('to_item')


    return render(request, 'pages/amaliyot-detail.html', {
        'tur': tur,
        'item': item,
        'related_items': related_items
    })

def kutubxona(request, cat_id=None):
    manbalar = KutubxonaCategory.objects.all()
    items = KutubxonaItem.objects.filter(is_active=True)

    active_category = None

    if cat_id:
        active_category = get_object_or_404(KutubxonaCategory, id=cat_id)
        items = items.filter(category=active_category)


    return render(request, 'pages/kutubxona.html', {'manbalar': manbalar, 'items': items, 'active_category': active_category})

def kutubxona_file_view(request, pk):
    item = get_object_or_404(KutubxonaItem, pk=pk, is_active=True)

    file_path = item.file.path
    mime_type, _ = mimetypes.guess_type(file_path)

    # Agar Word bo‘lsa — yuklab olish
    if mime_type in [
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ]:
        return FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            filename=item.file.name
        )

    # PDF va boshqalar — ko‘rish
    return FileResponse(
        open(file_path, 'rb'),
        content_type=mime_type,
        as_attachment=False
    )


def course_detail(request,slug):
    course = Course.objects.prefetch_related('modules__lessons').get(slug=slug)
    quiz = CourseTest.objects.filter(course=course).first()
    quiz_result = None
    enrolled = None
    course_progress = 0
    if request.user.is_authenticated:
        enrolled = CourseEnrollment.objects.filter(
            user=request.user,
            course=course
        ).first()
        if enrolled:
            course_progress = enrolled.progress
    active_lesson = Lesson.objects.filter(
        module__course=course
    ).first()

    if request.user.is_authenticated and quiz:
        quiz_result = QuizResult.objects.filter(
            user=request.user,
            quiz=quiz
        ).first()
    return render(request, 'pages/course-detail.html', {'course': course,'enrolled': enrolled, 'active_lesson': active_lesson, 'quiz_result':quiz_result, 'course_progress': course_progress})
@login_required
def mark_lesson_complete(request, lesson_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(['POST'])

    lesson = get_object_or_404(Lesson, id=lesson_id)

    enrollment = get_object_or_404(
        CourseEnrollment,
        user=request.user,
        course=lesson.module.course
    )

    progress_obj, created = LessonProgress.objects.get_or_create(
        enrollment=enrollment,
        lesson=lesson
    )

    if not progress_obj.is_completed:
        progress_obj.is_completed = True
        progress_obj.completed_at = timezone.now()
        progress_obj.save()

        # 🔥 ENG MUHIM QISM
        enrollment.get_course_progress()

    return JsonResponse({"status": "ok"})

@login_required
def course_test(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    enrollment = get_object_or_404(
        CourseEnrollment,
        user=request.user,
        course=course
    )

    # ❌ agar kurs tugamagan bo‘lsa
    if enrollment.get_course_progress() < 100:
        return redirect('inclusive_app:course_detail', slug=course.slug)

    quiz = get_object_or_404(CourseTest, course=course)
    if request.method == 'POST':
        correct = 0
        total = quiz.questions.count()

        for question in quiz.questions.all():
            selected = request.POST.get(f'question_{question.id}')
            if selected:
                answer = Answer.objects.get(id=selected)
                if answer.is_correct:
                    correct += 1

        score = int((correct / total) * 100)
        passed = score >= quiz.min_percentage

        QuizResult.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            passed=passed
        )

        return redirect('inclusive_app:test_result', quiz.id)

    # agar test allaqachon topshirilgan bo‘lsa
    if QuizResult.objects.filter(user=request.user, quiz=quiz).exists():
        return redirect('inclusive_app:test_result', quiz.id)

    questions = quiz.questions.prefetch_related('answers')

    return render(request, 'pages/course-test.html', {
        'quiz': quiz,
        'questions': questions
    })
@login_required
def test_result(request, quiz_id):
    quiz = get_object_or_404(CourseTest, id=quiz_id)

    result = get_object_or_404(
        QuizResult,
        user=request.user,
        quiz=quiz
    )

    return render(request, 'pages/test-result.html', {
        'quiz': quiz,
        'result': result
    })


@login_required
def download_certificate(request, course_id):
    cert = get_object_or_404(
        Certificate,
        user=request.user,
        course_id=course_id
    )

    return FileResponse(
        cert.pdf.open(),
        as_attachment=True,
        filename=f"certificate_{cert.course.slug}.pdf"
    )

@login_required
def course_enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id, is_active=True)

    enrollment, created = CourseEnrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    if created:
        messages.success(request, "Siz kursga muvaffaqiyatli yozildingiz ✅")
    else:
        messages.info(request, "Siz allaqachon bu kursga yozilgansiz")

    return redirect('inclusive_app:course_detail', slug=course.slug)

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz. Xush kelibsiz!")
            if user.user_type == 'student':
                return redirect('inclusive_app:teacher_dashboard')  # keyin bu urlni yaratasiz
            else:
                return redirect('inclusive_app:teacher_dashboard')
        else:
            messages.error(request, "Iltimos, xatoliklarni tuzating.")
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def teacher_dashboard(request):
    certificates = Certificate.objects.filter(user=request.user).select_related('course')
    enrollments = CourseEnrollment.objects.filter(
        user=request.user
    ).select_related('course')
    natija = QuizResult.objects.filter(user=request.user)
    user = request.user
    return render(request, 'users/user-dashboard.html', {'user': user,'certificates': certificates, 'enrollments': enrollments,'natija': natija})

@login_required
def teacher_edit_dashboard(request,user_id):
    if request.user.id != user_id:
        return redirect('inclusive_app:user_dashboard')

    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('inclusive_app:teacher_dashboard')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'users/user-edit-dashboard.html', {'form': form})


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('inclusive_app:teacher_dashboard')

def login_user(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            return redirect('inclusive_app:admin_dashboard')
        return redirect('inclusive_app:index')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request, user)
            if user.is_superuser:
                return redirect('inclusive_app:admin_dashboard')  # keyin bu urlni yaratasiz
            else:
                return redirect('inclusive_app:teacher_dashboard')
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("inclusive_app:login_user")
