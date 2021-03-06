from django.conf.urls import url, include

from apps.merchant_file.utils_views import login_view
from apps.merchant_file.utils_views import register
from apps.merchant_file.utils_views import child_manage

urlpatterns = [
    # 登录
    url(r'^login/$',login_view.LoginView.as_view()),
    # 注册
    url(r'^register/$',register.RegistView.as_view()),
    # 子店管理
    url(r'^child_mer/$',child_manage.ChaildMerchantInfoManageView.as_view()),
]