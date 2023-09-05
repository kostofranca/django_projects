from django.shortcuts import render

context = {
    "bride" : "Hatice Beyza",
    "broom" : "Ahmet Kasım",
    "guest":"test_guest",
    "ist" : {
        "dugun" : {
            "event_name" : "Düğün",
            "date" : "28 Ekim 2023",
            "location" : {
                "name": "Beykoz Koru Sosyal Tesisleri",
                "address" : "Beykoz / İstanbul",
                "link" : "https://goo.gl/maps/Z3zmEbBEFD9TN7DW8"
            },
            "phrase": "Sizleri düğünümüzde de görmekten şeref duyarız."
        }
    },
    "ant" : {
        "kina": {
                "event_name" : "Kına",
                "date" : "",
                "location" : {
                    "name": "",
                    "address" : "",
                    "link" : ""
            },
            "phrase": ""
        },
        "dugun": {
                "event_name" : "Düğün",
            "date" : "",
            "location" : {
                "name": "",
                "address" : "",
                "link" : ""
            },
            "phrase": ""
            }
    }
}


# Create your views here.

def invite(request):

    invitation = {
        "context": context,
        "head" : "Davetlisiniz..."
    }

    return render(request, "invitio/index.html", invitation)

