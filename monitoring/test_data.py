import pprint
from urllib.request import urlopen
headers = {
    'Authorization': "Basic OWIzYWFhZmJhOWZlNGY0Yzk1YzNiZTNlMWZlYWFlMzE6",
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "0acb6f32-d856-44f4-9234-77c46981366b"
    }

#Ввести  tender_id вручну
tender_id = 'dfeccebeb82f4cb888c3e340d9cd5ced'

payload = {
  "data": {
    "reasons": [
      "public",
      "fiscal"
    ],
    "tender_id": tender_id,
    "procuringStages": [
      "awarding",
      "contracting"
    ],
    "parties": [
      {
        "contactPoint": {
          "name": "Oleksii Kovalenko",
          "telephone": "0440000000"
        },
        "identifier": {
          "scheme": "UA-EDR",
          "id": "40165856",
          "uri": "http://www.dkrs.gov.ua"
        },
        "name": "The State Audit Service of Ukraine",
        "roles": [
          "risk_indicator"
        ],
        "address": {
          "countryName": "Ukraine",
          "postalCode": "04070",
          "region": "Kyiv",
          "streetAddress": "Petra Sahaidachnoho St, 4",
          "locality": "Kyiv"
        }
      }
    ]
  }
}

payload2 = {
  "data": {
    "decision": {
      "date": "2018-01-02T01:05:00",
      "description": "Опис підстав для здійсненнjjjjjjjjjjjjjjjjjjjjjjjjя моніторинг"
    }
  }
}

activate = {
  "data": {
    "status": "active"
  }
}

msg = {
  "data": {
    "title": "Тайтл диалога5",
    "description": "Описание диалога5"
  }
}


conclusion = {
  "data": {
    "conclusion": {
      "violationType": [
        "documentsForm",
        "corruptionAwarded"
      ],
      "description": "Ashes, ashes, we all fall down",
      "stringsAttached": "Pocket full of posies",
      "auditFinding": "Ring around the rosies",
      "violationOccurred": True
    }
  }
}

conclusion_for_declined = {
  "data": {
    "conclusion": {
      "violationType": [
        "documentsForm",
        "corruptionAwarded"
      ],
      "description": "Ось тиакивіалотів длескріпшн",
      "stringsAttached": "Pocket full of posies",
      "auditFinding": "Ring around the rosies",
      "violationOccurred": False
    }
  }
}


adressed = {
  "data": {
    "status": "addressed"
  }
}


stopped = {
  "data": {
    "status": "stopped",
    "cancellation": {
      "relatedParty": "be546d6519ee37a597df5c1ca71ddd18",
      "description": "Complaint was created"
    }
  }
}


complete = {
  "data": {
    "status": "completed"
  }
}


decline = {
  "data": {
    "status": "declined"
  }
}

eliminationResolution = {
  "data": {
    "eliminationResolution": {
      "description": "The award hasn't been fixed.",
      "relatedParty": "f0e119b94ed33bd9b72caf2573503984",
      "resultByType": {
        "corruptionAwarded": "not_eliminated",
        "documentsForm": "eliminated"
      },
      "result": "partly"
    }
  }
}