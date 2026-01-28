from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'inclusive_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login-user/', views.login_user, name='login_user'),
    path("logout/", views.user_logout, name="user_logout"),
    path('course-test/<int:course_id>/', views.course_test, name='course_test'),
    path('test-result/<int:quiz_id>/', views.test_result, name='test_result'),
    path('user-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('user-edit-dashboard/<int:user_id>', views.teacher_edit_dashboard, name='teacher_edit_dashboard'),
    path('dashboard/password/',views.UserPasswordChangeView.as_view(),name='password_change'),
    path('yangiliklar/<slug:slug>/', views.yangilik_detail, name='yangilik_detail'),
    path('course-detail/<slug:slug>/', views.course_detail, name='course_detail'),
    path('kurslar/', views.kurslar, name='kurslar'),
    path('kurslar/category/<int:cat_id>', views.kurslar, name='kurslar_category'),
    path('amaliyot/<slug:slug>/', views.amaliyot_items, name='amaliyot_items'),
    path('amaliyotitem-detail/<slug:tur_slug>/<slug:item_slug>', views.amaliyot_item_detail, name='amaliyot_item_detail'),
    path('lesson-complete/<int:lesson_id>/', views.mark_lesson_complete, name='mark_lesson_complete'),
    path('course-enroll/<int:course_id>/', views.course_enroll, name='course_enroll'),
    path('kutubxona/', views.kutubxona, name='kutubxona'),
    path('kutubxona/category/<int:cat_id>', views.kutubxona, name='kutubxona_category'),
    path('kutubxona/file/<int:pk>/',views.kutubxona_file_view,name='kutubxona_file_view'),
    path('certificate/<int:course_id>/', views.download_certificate, name='download_certificate'),
    # admin uchun
    path('manage-admin/', views.admin_dashboard, name='admin_dashboard'),
    # Course uchun
    path('admin-add-course/', views.admin_add_course, name='admin_add_course'),
    path('admin-edit-course/<int:course_id>', views.admin_add_course, name='admin_add_course'),
    path('admin-delete-course/<int:course_id>', views.admin_delete_course, name='admin_delete_course'),
    # Course Test uchun
    path('admin-add-coursetest/', views.admin_add_coursetest, name='admin_add_coursetest'),
    path('admin-edit-coursetest/<int:coursetest_id>', views.admin_add_coursetest, name='admin_add_coursetest'),
    path('admin-delete-coursetest/<int:coursetest_id>', views.admin_delete_coursetest, name='admin_delete_coursetest'),
    # Course module uchun
    path('admin-add-coursemodule/', views.admin_add_coursemodule, name='admin_add_coursemodule'),
    path('admin-edit-coursemodule/<int:coursemodule_id>', views.admin_add_coursemodule, name='admin_add_coursemodule'),
    path('admin-delete-coursemodule/<int:coursemodule_id>', views.admin_delete_coursemodule, name='admin_delete_coursemodule'),
    # Lesson uchun
    path('admin-add-lesson/', views.admin_add_lesson, name='admin_add_lesson'),
    path('admin-delete-lesson/<int:lesson_id>', views.admin_delete_lesson, name='admin_delete_lesson'),
    path('admin-edit-lesson/<int:lesson_id>', views.admin_add_lesson, name='admin_add_lesson'),
    # Course Enroll uchun
    path('admin-add-courseenrollement/', views.admin_add_courseenrollement, name='admin_add_courseenrollement'),
    path('admin-edit-courseenrollement/<int:courseenrollement_id>', views.admin_add_courseenrollement, name='admin_add_courseenrollement'),
    path('admin-delete-courseenrollement/<int:courseenrollement_id>', views.admin_delete_courseenrollement, name='admin_delete_courseenrollement'),
    # Course Progress uchun
    path('admin-course-progress/', views.admin_course_progress, name='admin_course_progress'),
    # Test Savollar uchun
    path('admin-add-question/', views.admin_add_question, name='admin_add_question'),
    path('admin-edit-question/<int:question_id>', views.admin_add_question, name='admin_add_question'),
    path('admin-delete-question/<int:question_id>', views.admin_delete_question, name='admin_delete_question'),
    # Javob uchun
    path('admin-add-variable/', views.admin_add_variable, name='admin_add_variable'),
    path('admin-edit-variable/<int:variable_id>', views.admin_add_variable, name='admin_add_variable'),
    path('admin-delete-variable/<int:variable_id>', views.admin_delete_variable, name='admin_delete_variable'),
    path('admin-add-user/', views.admin_add_user, name='admin_add_user'),
    path('admin-edit-user/<int:user_id>', views.admin_add_user, name='admin_add_user'),
    path('admin-delete-user/<int:user_id>', views.admin_delete_user, name='admin_delete_user'),
    # path('admin-sertificate-list/', views.admin_certificate_list, name='admin_certificate_list'),
    # Admin Amaliyot
    path('admin-add-amaliyot/', views.admin_add_amaliyot, name='admin_add_amaliyot'),
    path('admin-edit-amaliyot/<int:amaliyot_id>', views.admin_add_amaliyot, name='admin_add_amaliyot'),
    path('admin-delele-amaliyot/<int:amaliyot_id>', views.admin_delete_amaliyot, name='admin_delete_amaliyot'),
    path('admin-add-amaliyotitem/', views.admin_add_amaliyotitem, name='admin_add_amaliyotitem'),
    path('admin-edit-amaliyotitem/<int:amaliyotitem_id>', views.admin_add_amaliyotitem, name='admin_add_amaliyotitem'),
    path('admin-delele-amaliyotitem/<int:amaliyotitem_id>', views.admin_delete_amaliyotitem, name='admin_delete_amaliyotitem'),
    path('admin-add-amaliyotvideo/', views.admin_add_amaliyotvideo, name='admin_add_amaliyotvideo'),
    path('admin-edit-amaliyotvideo/<int:amaliyotvideo_id>', views.admin_add_amaliyotvideo, name='admin_add_amaliyotvideo'),
    path('admin-delele-amaliyotivideo<int:amaliyotvideo_id>', views.admin_delete_amaliyotvideo, name='admin_delete_amaliyotvideo'),
    path('admin-add-amaliyotsection/', views.admin_add_amaliyotsection, name='admin_add_amaliyotsection'),
    path('admin-edit-amaliyotsection/<int:amaliyotsection_id>', views.admin_add_amaliyotsection, name='admin_add_amaliyotsection'),
    path('admin-delele-amaliyotisection<int:amaliyotsection_id>', views.admin_delete_amaliyotsection, name='admin_delete_amaliyotsection'),
    path('admin-delele-amaliyotisection<int:amaliyotsection_id>', views.admin_delete_amaliyotsection, name='admin_delete_amaliyotsection'),
    path('admin-add-relatedamaliyot/', views.admin_add_relatedamaliyot, name='admin_add_relatedamaliyot'),
    path('admin-edit-relatedamaliyot/<int:relamal_id>', views.admin_add_relatedamaliyot, name='admin_add_relatedamaliyot'),
    path('admin-delete-relatedamaliyot/<int:relamal_id>', views.admin_delete_relatedamaliyot, name='admin_delete_relatedamaliyot'),
    # Yangiliklar uchun
    path('admin-add-yangiliklar/', views.admin_add_yangiliklar, name='admin_add_yangiliklar'),
    path('admin-edit-yangiliklar/<int:yangilik_id>', views.admin_add_yangiliklar, name='admin_add_yangiliklar'),
    path('admin-delete-yangiliklar/<int:yangilik_id>', views.admin_delete_yangiliklar, name='admin_delete_yangiliklar'),
    # Sahifa Rasmlari uchun
    path('admin-add-sahifarasm/', views.admin_add_sahifarasm, name='admin_add_sahifarasm'),
    path('admin-edit-sahifarasm/<int:sahifarasm_id>', views.admin_add_sahifarasm, name='admin_add_sahifarasm'),
    path('admin-delete-sahifarasm/<int:sahifarasm_id>', views.admin_delete_sahifarasm, name='admin_delete_sahifarasm'),
    # Kutubxona Bo'limi uchun
    path('admin-add-catkutubxona/', views.admin_add_catkutubxona, name='admin_add_catkutubxona'),
    path('admin-edit-catkutubxona/<int:catkutubxona_id>', views.admin_add_catkutubxona, name='admin_add_catkutubxona'),
    path('admin-delete-catkutubxona/<int:catkutubxona_id>', views.admin_delete_catkutubxona, name='admin_delete_catkutubxona'),
    # Kutubxona Manbalar uchun
    path('admin-add-mankutubxona/', views.admin_add_mankutubxona, name='admin_add_mankutubxona'),
    path('admin-edit-mankutubxona/<int:mankutubxona_id>', views.admin_add_mankutubxona, name='admin_add_mankutubxona'),
    path('admin-delete-mankutubxona/<int:mankutubxona_id>', views.admin_delete_mankutubxona, name='admin_delete_mankutubxona'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
