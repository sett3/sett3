from django.views.generic.base import TemplateView
from lab2.models import Members, Discography, Clipography


class IndexView(TemplateView):
    template_name = "index.html"
    Members.objects.all().delete()
    Members.objects.create(name="Levi", surname="Benton", instrument="", vocal="Extreme")
    Members.objects.create(name="B.J.", surname="Stead", instrument="Lead guitar", vocal="Backing")
    Members.objects.create(name="Justin", surname="Aufdemkampe", instrument="Rhythm guitar", vocal="")
    Members.objects.create(name="Ryan", surname="Neff", instrument="Bass guitar", vocal="Clean")
    Members.objects.create(name="Jerod", surname="Boyd", instrument="Drums", vocal="")
    Discography.objects.all().delete()
    Discography.objects.create(id=1, album="Apologies Are for the Weak", genre="Deathcore", year="2009", songs="10")
    Discography.objects.create(id=2, album="Monument", genre="Metalcore", year="2010", songs="10")
    Discography.objects.create(id=3, album="At Heart", genre="Melodic Metalcore", year="2012", songs="13")
    Discography.objects.create(id=4, album="Rise of the Lion", genre="Thrash metal/Metalcore", year="2014", songs="12")
    Discography.objects.create(id=5, album="Deathless", genre="Metalcore", year="2015", songs="10")
    Clipography.objects.all().delete()
    Clipography.objects.create(song="Forgive and Forget", album=Discography.objects.get(id=1), date="2009", director="Spencer Nicholson")
    Clipography.objects.create(song="Relentless Chaos", album=Discography.objects.get(id=2), date="2010", director="Thunder Down Country")
    Clipography.objects.create(song="Ballad of a Broken Man", album=Discography.objects.get(id=3), date="2012", director="Brad Golowin")
    Clipography.objects.create(song="Deathless", album=Discography.objects.get(id=5), date="2015", director="Max Moore")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'members_list': Members.objects.all(),
                'discs_list': Discography.objects.all(),
                'clips_list': Clipography.objects.all(),
            }
        )
        return context
