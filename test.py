import docx2pdf
from docxtpl import DocxTemplate
from docx2pdf import convert


doc = DocxTemplate("CV_WEVIOO.docx")
context ={
  "firstName": "Ali",
  "lastName": "Chaabane",
  "poste_occupe": "Ingénieur développement JAVA EE",
  "anciennete": " 2 ans d'experience",
  "competences": [
     {"competence": "Travail d'équipe "},{"competence": "Résolution de problèmes"},{"competence": "Gestion du temps"}
    ],
  "Formations": [
    {"date": "01/01/2020","formation": "Certification Spring/Angular 8"},
    {"date": "01/01/2019","formation": "Ingénierie en informatique - spécialité : système d’information Ecole nationale d’ingénieur de Carthage, Tunisie"},
    {"date": "01/01/2016","formation": "Licence fondamentale en informatique de gestion Faculté des sciences économiques et de gestion de Tunis"}
  ],
"competTech": [
    {
      "technologie": "Programmation",
      "valeur": [
        {
          "competence" : "Python"
        },
        {
          "competence" : "C++"
        },
        {
          "competence" : "Java"
        },
        {
          "competence" : "JavaScript"
        }
      ]
    },
    {
      "technologie": "Développement web",
      "valeur": [
        {
          "competence" : "HTML"
        },
        {
          "competence" : "CSS"
        },
        {
          "competence" : "React"
        },
        {
          "competence" : "Angular"
        }
      ]
    }
  ],


  "experiences": [
    {
      "date": "01/01/2023",
      "projet": "E-construction",
      "desc": "E-Construction Plateforme de gestion des demandes des permis de bâtir",
      "emp": "Wevioo",
      "client": "Le Panier Gourmand",
      "role": "Ingénieur développement JAVA EE",
      "activiter": [
        {
          "activ" : "Conception des différentes activités via Joget Workflow"
        },
        {
          "activ" : "Développement des interfaces utilisateur"
        },
        {
          "activ" : "Implémentation de code spécifique métier Java Bean Shell"
        }
      ],
      "envi": [
        {
          "env" : "Joget"
        },
        {
          "env" : "java"
        },
        {
          "env" : "Hibernate"
        },
        {
          "env": "JQuery"
        },
        {
          "env": "XPDL"
        },
        {
          "env": "JavaScript"
        },
        {
          "env": "HTML"
        }
      ]
    },
    {
      "date": "01/01/2023",
      "projet": "E-construction",
      "desc": "E-Construction Plateforme de gestion des demandes des permis de bâtir",
      "emp": "Wevioo",
      "client": "Le Panier Gourmand",
      "role": "Ingénieur développement JAVA EE",
      "activiter": [
        {
          "activ" : "Conception des différentes activités via Joget Workflow"
        },
        {
          "activ" : "Développement des interfaces utilisateur"
        },
        {
          "activ" : "Implémentation de code spécifique métier Java Bean Shell"
        }
      ],
      "envi": [
        {
          "env" : "Joget"
        },
        {
          "env" : "java"
        },
        {
          "env" : "Hibernate"
        },
        {
          "env": "JQuery"
        },
        {
          "env": "XPDL"
        },
        {
          "env": "JavaScript"
        },
        {
          "env": "HTML"
        }
      ]
    }
  ],

    "Langues": [
      {
        "langue": "Francer","niveau": "Très bien"
      },
      {
        "langue": "Anglais","niveau": "Très bien"
      },
      {
        "langue": "Arabe","niveau": "Courant(e)"
      }
    ]
}


doc.render(context)
doc.save("outpout_tamplate.docx")

#convert("outpout_tamplate.docx","outpout_tamplate.pdf")






