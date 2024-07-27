from .models import SiteSetup

def example(request):
    return {
        "example": "vei do do example"
    }
    
def site_setup(request):
    setup = SiteSetup.objects.order_by("-id").first()
    return {
        "site_setup": setup
    }