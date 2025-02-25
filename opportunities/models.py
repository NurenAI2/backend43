from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account
from contacts.models import Contact
from django.conf import settings
from tenant.models import Tenant 
from leads.models import Stage

STAGES = (
    ('QUALIFICATION', 'QUALIFICATION'),
    ('NEEDS ANALYSIS', 'NEEDS ANALYSIS'),
    ('VALUE PROPOSITION', 'VALUE PROPOSITION'),
    ('ID.DECISION MAKERS', 'ID.DECISION MAKERS'),
    ('PERCEPTION ANALYSIS', 'PERCEPTION ANALYSIS'),
    ('PROPOSAL/PRICE QUOTE', 'PROPOSAL/PRICE QUOTE'),
    ('NEGOTIATION/REVIEW', 'NEGOTIATION/REVIEW'),
    ('CLOSED WON', 'CLOSED WON'),
    ('CLOSED LOST', 'CLOSED LOST'),
)

SOURCES = (
    ('NONE', 'NONE'),
    ('CALL', 'CALL'),
    ('EMAIL', ' EMAIL'),
    ('EXISTING CUSTOMER', 'EXISTING CUSTOMER'),
    ('PARTNER', 'PARTNER'),
    ('PUBLIC RELATIONS', 'PUBLIC RELATIONS'),
    ('CAMPAIGN', 'CAMPAIGN'),
    ('WEBSITE', 'WEBSITE'),
    ('OTHER', 'OTHER'),
)



TYPECHOICES = (
    ('CUSTOMER', 'CUSTOMER'),
    ('INVESTOR', 'INVESTOR'),
    ('PARTNER', 'PARTNER'),
    ('RESELLER', 'RESELLER'),
)

INDCHOICES = (
    ('ADVERTISING', 'ADVERTISING'),
    ('AGRICULTURE', 'AGRICULTURE'),
    ('APPAREL & ACCESSORIES', 'APPAREL & ACCESSORIES'),
    ('AUTOMOTIVE', 'AUTOMOTIVE'),
    ('BANKING', 'BANKING'),
    ('BIOTECHNOLOGY', 'BIOTECHNOLOGY'),
    ('BUILDING MATERIALS & EQUIPMENT', 'BUILDING MATERIALS & EQUIPMENT'),
    ('CHEMICAL', 'CHEMICAL'),
    ('COMPUTER', 'COMPUTER'),
    ('EDUCATION', 'EDUCATION'),
    ('ELECTRONICS', 'ELECTRONICS'),
    ('ENERGY', 'ENERGY'),
    ('ENTERTAINMENT & LEISURE', 'ENTERTAINMENT & LEISURE'),
    ('FINANCE', 'FINANCE'),
    ('FOOD & BEVERAGE', 'FOOD & BEVERAGE'),
    ('GROCERY', 'GROCERY'),
    ('HEALTHCARE', 'HEALTHCARE'),
    ('INSURANCE', 'INSURANCE'),
    ('LEGAL', 'LEGAL'),
    ('MANUFACTURING', 'MANUFACTURING'),
    ('PUBLISHING', 'PUBLISHING'),
    ('REAL ESTATE', 'REAL ESTATE'),
    ('SERVICE', 'SERVICE'),
    ('SOFTWARE', 'SOFTWARE'),
    ('SPORTS', 'SPORTS'),
    ('TECHNOLOGY', 'TECHNOLOGY'),
    ('TELECOMMUNICATIONS', 'TELECOMMUNICATIONS'),
    ('TELEVISION', 'TELEVISION'),
    ('TRANSPORTATION', 'TRANSPORTATION'),
    ('VENTURE CAPITAL', 'VENTURE CAPITAL'),
)

class Opportunity(models.Model):
    name = models.CharField(max_length=64)
    account = models.ForeignKey(Account, related_name='opportunities', on_delete=models.CASCADE, blank=True, null=True)
    stage = models.CharField( max_length=64, choices=STAGES)
    stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField("Opportunity Amount", decimal_places=2, max_digits=12, blank=True, null=True)
    lead_source = models.CharField("Source of Lead", max_length=255, choices=SOURCES, blank=True, null=True)
    probability = models.IntegerField(default=0, blank=True, null=True)
    contacts = models.ForeignKey(Contact, related_name='opportunity', on_delete=models.CASCADE, blank=True, null=True)
    closedBy = models.CharField(max_length=255, blank=True, null=True)
    closedOn = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdBy = models.CharField(max_length=255, blank=True, null=True)
    createdOn = models.DateTimeField("Created on", auto_now_add=True)
    isActive = models.BooleanField(default=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


