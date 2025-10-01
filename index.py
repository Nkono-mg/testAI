import json

samples = [
    {
        "input": {
            "cible": {
                "nom": "Jean Dupont",
                "poste": "Directeur Commercial",
                "entreprise": "TechCorp",
                "secteur": "Technologie"
            },
            "contextes": [
                "Jean Dupont a récemment pris ses fonctions de Directeur Commercial chez TechCorp.",
                "TechCorp développe des solutions SaaS pour les PME en pleine croissance.",
                "Le secteur technologique est en forte expansion sur la transformation digitale."
            ],
            "categories": {"parent": "Contenu professionnel", "enfant": "Succès et parcours"},
            "proposition_valeur": "Notre plateforme aide les entreprises technologiques à générer plus de leads qualifiés via des campagnes automatisées.",
            "raisonnement_commercial": "Nouvelle prise de poste = besoin de solutions efficaces pour booster rapidement les ventes."
        },
        "output": {
            "accroche": "Félicitations pour votre récente prise de poste chez TechCorp ! Un rôle stimulant qui s’accompagne de grands défis commerciaux.",
            "proposition_valeur": "Notre plateforme peut vous aider à accélérer la génération de leads qualifiés et à atteindre vos objectifs rapidement."
        }
    },
    {
        "input": {
            "cible": {
                "nom": "Sophie Martin",
                "poste": "Responsable RH",
                "entreprise": "HealthCare Plus",
                "secteur": "Médecine"
            },
            "contextes": [
                "Sophie Martin a publié un article sur LinkedIn concernant le bien-être des employés.",
                "HealthCare Plus est un réseau de cliniques privées innovant.",
                "Le secteur médical met l’accent sur l’intégration de solutions digitales pour la gestion RH."
            ],
            "categories": {"parent": "Résumé professionnel", "enfant": "Expériences"},
            "proposition_valeur": "Notre solution optimise la communication interne et améliore l’engagement des collaborateurs.",
            "raisonnement_commercial": "Une responsable RH dans le secteur médical cherche à renforcer la cohésion et réduire le turnover."
        },
        "output": {
            "accroche": "J’ai beaucoup apprécié votre article sur le bien-être au travail, un sujet clé dans le secteur médical.",
            "proposition_valeur": "Notre solution pourrait vous aider à renforcer l’engagement des collaborateurs et à fluidifier vos processus RH."
        }
    },
    {
        "input": {
            "cible": {
                "nom": "Ali Ben Ahmed",
                "poste": "CTO",
                "entreprise": "InnoWeb Services",
                "secteur": "Services Internet"
            },
            "contextes": [
                "Ali Ben Ahmed partage régulièrement des articles techniques sur LinkedIn.",
                "InnoWeb Services propose des services cloud et de cybersécurité.",
                "Le secteur internet est en constante évolution avec une demande accrue en solutions sécurisées."
            ],
            "categories": {"parent": "Contenu professionnel", "enfant": "Technologies et innovations"},
            "proposition_valeur": "Nous aidons les CTO à sécuriser leurs infrastructures tout en améliorant la performance de leurs systèmes.",
            "raisonnement_commercial": "Un CTO de services internet doit gérer à la fois innovation et cybersécurité."
        },
        "output": {
            "accroche": "J’ai remarqué vos publications sur l’innovation technologique et la sécurité, des enjeux majeurs pour InnoWeb.",
            "proposition_valeur": "Notre solution pourrait vous permettre de renforcer vos infrastructures cloud tout en garantissant leur performance."
        }
    },
    {
        "input": {
            "cible": {
                "nom": "Maria Lopez",
                "poste": "Directrice Marketing",
                "entreprise": "EcoFashion",
                "secteur": "Mode durable"
            },
            "contextes": [
                "Maria Lopez a récemment partagé un post sur LinkedIn concernant la mode éthique.",
                "EcoFashion est une marque spécialisée dans le textile éco-responsable.",
                "Le secteur de la mode durable attire de plus en plus de consommateurs sensibles à l’environnement."
            ],
            "categories": {"parent": "Résumé professionnel", "enfant": "Valeurs et convictions"},
            "proposition_valeur": "Notre plateforme permet de créer des campagnes marketing personnalisées mettant en avant les engagements RSE.",
            "raisonnement_commercial": "Une directrice marketing dans la mode durable doit mettre en valeur l’éthique de la marque."
        },
        "output": {
            "accroche": "Votre engagement pour une mode plus responsable est inspirant et attire l’attention des consommateurs.",
            "proposition_valeur": "Nous pouvons vous accompagner dans la création de campagnes personnalisées qui valorisent vos engagements RSE."
        }
    },
    {
        "input": {
            "cible": {
                "nom": "David Johnson",
                "poste": "CEO",
                "entreprise": "GreenEnergy Solutions",
                "secteur": "Énergies renouvelables"
            },
            "contextes": [
                "David Johnson a annoncé sur LinkedIn le lancement d’un nouveau projet solaire.",
                "GreenEnergy Solutions développe des solutions innovantes en énergie renouvelable.",
                "Le secteur des énergies renouvelables est en pleine croissance et attire de nouveaux investisseurs."
            ],
            "categories": {"parent": "Contenu professionnel", "enfant": "Projets et réussites"},
            "proposition_valeur": "Notre entreprise propose des outils d’analyse pour optimiser la rentabilité et la visibilité des projets verts.",
            "raisonnement_commercial": "Un CEO dans les énergies renouvelables cherche à attirer investisseurs et partenaires."
        },
        "output": {
            "accroche": "Félicitations pour le lancement de votre nouveau projet solaire, une avancée importante pour GreenEnergy Solutions.",
            "proposition_valeur": "Nos outils peuvent vous aider à maximiser la rentabilité et la visibilité de vos projets dans le domaine des énergies renouvelables."
        }
    }
]

#creating and writting jsonl file
with open("samples.jsonl", "w", encoding="utf-8") as f:
    for sample in samples:
        f.write(json.dumps(sample, ensure_ascii=False) + "\n")

print("samples.jsonl generated succefful !")
