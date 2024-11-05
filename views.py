from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from django.http import HttpResponse
from django.views.decorators.http import require_GET


class RobotsTxtView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


class YandexView(TemplateView):
    template_name = 'yandex_231c829d9a86caa9.html'


class SitemapXmlView(TemplateView):
    template_name = 'sitemapxml.html'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.filter(is_published=True).order_by('-time_create')
        #context['services'] = Services.objects.all()
        #context['projects'] = Project.objects.all()
        return context


class Index(ListView):
    queryset = News.objects.all()
    template_name = "center/index.html"
    model = News
    
    
    @staticmethod
    def news_all_index():
        news_all_index = News.objects.all().order_by('-time_create')
        return news_all_index


class Search(ListView):
    model = Documents
    template_name = 'center/search-results.html'
    context_object_name = 'docs'
    paginate_by = 5

    def get_queryset(self):
        search = self.request.GET.get('q')
        documents_all = Documents.objects.all()
        queryset = documents_all.filter(title__istartswith=search) | documents_all.filter(title__iregex=search)
        return queryset

    @staticmethod
    def news_all_search_results():
        news_all = News.objects.all().order_by('-time_create')[:3]
        return news_all
        
        
class News_all(ListView):
    queryset = News.objects.all()
    template_name = "center/blog.html"
    model = News
    
    @staticmethod
    def news_all_news():
        news_all = News.objects.all().order_by('-time_create')
        return news_all


class ShowNews(DetailView):
    model = News
    template_name = 'center/news-view.html'
    slug_url_kwarg = 'news_slug'
    context_object_name = 'news'
    
    @staticmethod
    def news_all_show_news():
        news_all = News.objects.all().order_by('-time_create')[:3]
        return news_all
    
    
class Fdocs_gia11(ListView):
    queryset = Documents.objects.all()
    template_name = "center/fdocs-gia11.html"
    model = Documents

    @staticmethod
    def news_all_fdocs_gia11():
        news_all = News.objects.all().order_by('-time_create')[:3]
        return news_all

    @staticmethod
    def docs_all_fdocs_gia11():
        docs_all = Documents.objects.filter(section__id=14).order_by('-time_update')
        return docs_all


class Rdocs_gia11(ListView):
    queryset = Documents.objects.all()
    template_name = "center/rdocs-gia11.html"
    model = Documents

    @staticmethod
    def news_all_rdocs_gia11():
        news_all = News.objects.all().order_by('-time_create')[:3]
        return news_all

    @staticmethod
    def docs_all_rdocs_gia11():
        docs_all = Documents.objects.filter(section__id=15).order_by('-time_update')
        return docs_all



class Fdocs_gia9(ListView):
    queryset = Documents.objects.all()
    template_name = "center/fdocs-gia9.html"
    model = Documents

    @staticmethod
    def news_all_fdocs_gia9():
        news_all = News.objects.all().order_by('-time_create')[:3]
        return news_all

    @staticmethod
    def docs_all_fdocs_gia9():
        docs_all = Documents.objects.filter(section__id=1).order_by('-time_update')
        return docs_all


class Rdocs_gia9(ListView):
    queryset = Documents.objects.all()
    template_name = "center/rdocs-gia9.html"
    model = Documents

    @staticmethod
    def news_all_rdocs_gia9():
        news_all = News.objects.all().order_by('-time_create')[:3]
        return news_all

    @staticmethod
    def docs_all_rdocs_gia9():
        docs_all = Documents.objects.filter(section__id=2).order_by('-time_update')
        return docs_all
        
     
class Guidelines_gia9(ListView):
    queryset = Documents.objects.all()
    template_name = "center/guidelines-gia9.html"
    model = Documents

    @staticmethod
    def news_all_guidelines_gia9():
        news_all = News.objects.all().order_by('-time_create')[:3]
        return news_all

    @staticmethod
    def docs_all_guidelines_gia9():
        docs_all = Documents.objects.filter(section__id=39).order_by('-time_update')
        return docs_all
        

class Guidelines_gia11(ListView):
    queryset = Documents.objects.all()
    template_name = "center/guidelines-gia11.html"
    model = Documents

    @staticmethod
    def news_all_guidelines_gia11():
        news_all = News.objects.all().order_by('-time_create')[:3]
        return news_all

    @staticmethod
    def docs_all_guidelines_gia11():
        docs_all = Documents.objects.filter(section__id=40).order_by('-time_update')
        return docs_all
        
        
class Sobes_gia9(ListView):
    queryset = Documents.objects.all()
    template_name = "center/sobes-gia9.html"
    model = Documents

    @staticmethod
    def news_all_sobes_gia9():
        news_all_sobes_gia9 = News.objects.all().order_by('-time_create')[:3]
        return news_all_sobes_gia9

    @staticmethod
    def docs_all_sobes_gia9():
        docs_all = Documents.objects.all()
        return docs_all
        
    @staticmethod
    def docs_all_sobes_gia9_reglament():
        docs_all = Documents.objects.filter(section__id=3).order_by('-time_update')
        return docs_all
        
    @staticmethod
    def docs_all_sobes_gia9_audio():
        docs_all = Documents.objects.filter(section__id=8).order_by('-time_update')
        return docs_all
        
    @staticmethod
    def docs_all_sobes_gia9_mr():
        docs_all = Documents.objects.filter(section__id=4).order_by('-time_update')
        return docs_all
        
    @staticmethod
    def docs_all_sobes_gia9_instr():
        docs_all = Documents.objects.filter(section__id=5).order_by('-time_update')
        return docs_all 
        
    @staticmethod
    def docs_all_sobes_gia9_sbornik():
        docs_all = Documents.objects.filter(section__id=6).order_by('-time_update')
        return docs_all 
        
    @staticmethod
    def docs_all_sobes_gia9_npa():
        docs_all = Documents.objects.filter(section__id=7).order_by('-time_update')
        return docs_all   
        
    
class Info_gia9(ListView):
    queryset = Documents.objects.all()
    template_name = "center/information-for-participants-gia9.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_info_gia9():
        news_all_sobes_gia9 = News.objects.all().order_by('-time_create')[:3]
        return news_all_sobes_gia9

    @staticmethod
    def docs_all_info_gia9():
        docs_all = Documents.objects.filter(section__id=9).order_by('-time_update')
        return docs_all


class Raspisanie_gia9(ListView):
    queryset = Documents.objects.all()
    template_name = "center/raspisanie-gia9.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_raspisanie_gia9():
        news_all_sobes_gia9 = News.objects.all().order_by('-time_create')[:3]
        return news_all_sobes_gia9

    @staticmethod
    def docs_all_raspisanie_gia9():
        docs_all = Documents.objects.filter(section__id=10).order_by('-time_update')
        return docs_all
        

class Obrazcy_blankov_gia9(ListView):
    queryset = Documents.objects.reverse()
    template_name = "center/obrazcy-blankov-gia9.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_obrazcy_blankov_gia9():
        news_all_obrazcy_blankov = News.objects.all().order_by('-time_create')[:3]
        return news_all_obrazcy_blankov

    @staticmethod
    def docs_all_obrazcy_blankov_gia9():
        docs_all = Documents.objects.filter(section__id=11).order_by('-time_update')
        return docs_all
        

class Specz_usloviya_gia9(ListView):
    queryset = Documents.objects.all()
    template_name = "center/specz-usloviya-gia9.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_specz_usloviya_gia9():
        news_all_obrazcy_blankov = News.objects.all().order_by('-time_create')[:3]
        return news_all_obrazcy_blankov

    @staticmethod
    def docs_all_specz_usloviya_gia9():
        docs_all = Documents.objects.filter(section__id=12).order_by('-time_update')
        return docs_all
        

class Podgotovka_kadrov_gia9(ListView):
    queryset = Documents.objects.all()
    template_name = "center/podgotovka-kadrov-gia9.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_podgotovka_kadrov_gia9():
        news_all_podgotovka_kadrov = News.objects.all().order_by('-time_create')[:3]
        return news_all_podgotovka_kadrov

    @staticmethod
    def docs_all_podgotovka_kadrov_gia9():
        docs_all = Documents.objects.filter(section__id=13).order_by('-time_update')
        return docs_all


class Presentation_gia11(ListView):
    queryset = Documents.objects.all().reverse()
    template_name = "center/presentation-gia11.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_presentation_gia11():
        news_all_presentation_gia11 = News.objects.all().order_by('-time_create')[:3]
        return news_all_presentation_gia11

    @staticmethod
    def docs_all_presentation_gia11_general_information():
        docs_all = Documents.objects.filter(section__id=16).order_by('-time_update')
        return docs_all

    @staticmethod
    def docs_all_presentation_gia11_place_registration():
        docs_all = Documents.objects.filter(section__id=34).order_by('-time_update')
        return docs_all

    @staticmethod
    def docs_all_presentation_gia11_submission_applications():
        docs_all = Documents.objects.filter(section__id=35).order_by('-time_update')
        return docs_all

    @staticmethod
    def docs_all_presentation_gia11_plan_schedule():
        docs_all = Documents.objects.filter(section__id=36).order_by('-time_update')
        return docs_all

    @staticmethod
    def docs_all_presentation_gia11_sample_forms():
        docs_all = Documents.objects.filter(section__id=37).order_by('-time_update')
        return docs_all

    @staticmethod
    def docs_all_presentation_gia11_instructional_materials():
        docs_all = Documents.objects.filter(section__id=38).order_by('-time_update')
        return docs_all



class Raspisanie_gia11(ListView):
    queryset = Documents.objects.all()
    template_name = "center/raspisanie-gia11.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_raspisanie_gia11():
        news_all_raspisanie_gia11 = News.objects.all().order_by('-time_create')[:3]
        return news_all_raspisanie_gia11

    @staticmethod
    def docs_all_raspisanie_gia11():
        docs_all = Documents.objects.filter(section__id=18).order_by('-time_update')
        return docs_all
        

class Info_gia11(ListView):
    queryset = Documents.objects.all()
    template_name = "center/information-for-participants-gia11.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_info_gia11():
        news_all_info_gia11 = News.objects.all().order_by('-time_create')[:3]
        return news_all_info_gia11

    @staticmethod
    def docs_all_info_gia11():
        docs_all = Documents.objects.filter(section__id=17).order_by('-time_update')
        return docs_all


class Obrazcy_blankov_gia11(ListView):
    queryset = Documents.objects.all()
    template_name = "center/obrazcy-blankov-gia11.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_obrazcy_blankov_gia11():
        news_all_obrazcy_blankov = News.objects.all().order_by('-time_create')[:3]
        return news_all_obrazcy_blankov

    @staticmethod
    def docs_all_obrazcy_blankov_gia11():
        docs_all = Documents.objects.filter(section__id=19).order_by('-time_update')
        return docs_all


class Specz_usloviya_gia11(ListView):
    queryset = Documents.objects.all()
    template_name = "center/specz-usloviya-gia11.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_specz_usloviya_gia11():
        news_all_specz_usloviya = News.objects.all().order_by('-time_create')[:3]
        return news_all_specz_usloviya

    @staticmethod
    def docs_all_specz_usloviya_gia11():
        docs_all = Documents.objects.filter(section__id=20).order_by('-time_update')
        return docs_all


class Podgotovka_kadrov_gia11(ListView):
    queryset = Documents.objects.all()
    template_name = "center/podgotovka-kadrov-gia11.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_podgotovka_kadrov_gia11():
        news_all_podgotovka_kadrov = News.objects.all().order_by('-time_create')[:3]
        return news_all_podgotovka_kadrov

    @staticmethod
    def docs_all_podgotovka_kadrov_gia11():
        docs_all = Documents.objects.filter(section__id=21).order_by('-time_update')
        return docs_all


class Training_events(ListView):
    queryset = Documents.objects.all()
    template_name = "center/training-events.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_training_events():
        news_all_training_events = News.objects.all().order_by('-time_create')[:3]
        return news_all_training_events

    @staticmethod
    def docs_all_training_events():
        docs_all = Documents.objects.filter(section__id=22).order_by('-time_update')
        return docs_all


class Training_events_general_info(ListView):
    queryset = Documents.objects.all()
    template_name = "center/training-events-general-info.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_training_events_general_info():
        news_all_training_events_general_info = News.objects.all().order_by('-time_create')[:3]
        return news_all_training_events_general_info

    @staticmethod
    def docs_all_training_events_general_info():
        docs_all = Documents.objects.filter(section__id=23).order_by('-time_update')
        return docs_all
        

class Fdocs_education_quality_assessment(ListView):
    queryset = Documents.objects.all()
    template_name = "center/fdocs-education-quality-assessment.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_fdocs_education_quality_assessment():
        news_all_fdocs_education_quality_assessment = News.objects.all().order_by('-time_create')[:3]
        return news_all_fdocs_education_quality_assessment

    @staticmethod
    def docs_all_fdocs_education_quality_assessment():
        docs_all = Documents.objects.filter(section__id=24).order_by('-time_update')
        return docs_all


class Rdocs_education_quality_assessment(ListView):
    queryset = Documents.objects.all()
    template_name = "center/rdocs-education-quality-assessment.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_rdocs_education_quality_assessment():
        news_all_rdocs_education_quality_assessment = News.objects.all().order_by('-time_create')[:3]
        return news_all_rdocs_education_quality_assessment

    @staticmethod
    def docs_all_rdocs_education_quality_assessment():
        docs_all = Documents.objects.filter(section__id=25).order_by('-time_update')
        return docs_all


class Testing_work(ListView):
    queryset = Documents.objects.all()
    template_name = "center/testing-work.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_testing_work():
        news_all_testing_work = News.objects.all().order_by('-time_create')[:3]
        return news_all_testing_work

    @staticmethod
    def docs_all_testing_work():
        docs_all = Documents.objects.filter(section__id=26).order_by('-time_update')
        return docs_all



class Other_studies(ListView):
    queryset = Documents.objects.all()
    template_name = "center/other-studies.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_other_studies():
        news_all_other_studies = News.objects.all().order_by('-time_create')[:3]
        return news_all_other_studies

    @staticmethod
    def docs_all_other_studies():
        docs_all = Documents.objects.filter(section__id=27).order_by('-time_update')
        return docs_all


class Activity(ListView):
    queryset = Documents.objects.all()
    template_name = "center/activity.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_activity():
        news_all_activity = News.objects.all().order_by('-time_create')[:3]
        return news_all_activity

    @staticmethod
    def docs_all_activity():
        docs_all = Documents.objects.filter(section__id=28).order_by('-time_update')
        return docs_all


class Hotline(ListView):
    queryset = Documents.objects.all()
    template_name = "center/hotline.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_hotline():
        news_all_hotline = News.objects.all().order_by('-time_create')[:3]
        return news_all_hotline

    @staticmethod
    def docs_all_hotline():
        docs_all = Documents.objects.filter(section__id=29).order_by('-time_update')
        return docs_all
        

class Webinars(ListView):
    queryset = Documents.objects.all()
    template_name = "center/webinars.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_webinars():
        news_all_webinars = News.objects.all().order_by('-time_create')[:3]
        return news_all_webinars

    @staticmethod
    def docs_all_webinars():
        docs_all = Documents.objects.filter(section__id=30).order_by('-time_update')
        return docs_all
        

class Constituent_documents(ListView):
    queryset = Documents.objects.all()
    template_name = "center/constituent-documents.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_constituent_documents():
        news_all_constituent_documents = News.objects.all().order_by('-time_create')[:3]
        return news_all_constituent_documents

    @staticmethod
    def docs_all_constituent_documents():
        docs_all = Documents.objects.filter(section__id=31).order_by('-time_update')
        return docs_all


class Local_acts(ListView):
    queryset = Documents.objects.all()
    template_name = "center/local-acts.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_local_acts():
        news_all_local_acts = News.objects.all().order_by('-time_create')[:3]
        return news_all_local_acts

    @staticmethod
    def docs_all_local_acts():
        docs_all = Documents.objects.filter(section__id=32).order_by('-time_update')
        return docs_all


class Services(ListView):
    queryset = Documents.objects.all()
    template_name = "center/services.html"
    model = Documents
    context_object_name = 'docs'

    @staticmethod
    def news_all_services():
        news_all_services = News.objects.all().order_by('-time_create')[:3]
        return news_all_services

    @staticmethod
    def docs_all_services():
        docs_all = Documents.objects.filter(section__id=33).order_by('-time_update')
        return docs_all
        
        
class Contacts(ListView):
    queryset = Documents.objects.all()
    template_name = "center/contacts.html"
    model = Documents
    

def update_csv_data_view(request):
    update_csv_data()

    return HttpResponse('Импорт результатов ЕГЭ/ОГЭ завершен')
    


