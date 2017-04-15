#(C) Copyright Syd Logan 2017
#(C) Copyright Thousand Smiles Foundation 2016
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

from django.conf.urls import url
from register.views import RegisterView

urlpatterns = [
    url(r'^$', RegisterView.as_view()),
    url(r'^([0-9]+)/$', RegisterView.as_view()),
]