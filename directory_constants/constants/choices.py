from directory_constants.constants import lead_generation, sectors


SPECIFIC = 'specific'
OPEN_ENDED = 'open_ended'
DISTRIBUTION = 'distribution'
WHOLESALE = 'wholesale'
RETAIL = 'retail'
HOSPITALITY = 'hospitality'
CATERING = 'catering'
MANUFACTURING = 'manufacturing'

TYPE_OF_ENQUIRIES = (
    (SPECIFIC, 'Specific'),
    (OPEN_ENDED, 'Open-ended'),
)

FOOD_LEAD_GENERATION_BUSINESS_MODELS = (
    (DISTRIBUTION, 'Distribution'),
    (WHOLESALE, 'Wholesale'),
    (RETAIL, 'Retail'),
)

FOOD_LEAD_GENERATION_SECTORS = (
    (RETAIL, 'Retail'),
    (HOSPITALITY, 'Hospitality'),
    (CATERING, 'Catering'),
    (MANUFACTURING, 'Manufacturing'),
)

LEGAL_LEAD_GENERATION_SECTORS = (
    (sectors.TECHNOLOGY, 'Technology'),
    (sectors.FOOD_AND_DRINK, 'Food and drink'),
    (sectors.RETAIL_AND_LUXURY, 'Retail'),
    (
        sectors.FINANCIAL_AND_PROFESSIONAL_SERVICES,
        (
            'Professional services (for example, financial '
            'services or business consulting'
        )
    ),
    (sectors.MARINE, 'Marine'),
    (sectors.ENERGY, 'Energy'),
)

LEGAL_LEAD_GENERATION_NEED = (
    (
        'General-business-advice-and-partnership',
        'General business advice and partnership'
    ),
    ('Business-start-up-advice', 'Business start-up advice'),
    ('Drafting-of-contracts', 'Drafting of contracts'),
    ('Mergers-and-acquisitions', 'Mergers and acquisitions'),
    ('Immigration', 'Immigration'),
    ('Dispute-resolution', 'Dispute resolution'),
)

LEAD_GENERATION_EXPORT_DESTINATIONS = (
    ('CN', 'China'),
    ('DE', 'Germany'),
    ('IN', 'India'),
    ('JP', 'Japan'),
    ('US', 'United States'),
)

INDUSTRIES = (
    (sectors.AEROSPACE, 'Aerospace'),
    (sectors.ADVANCED_MANUFACTURING, 'Advanced manufacturing'),
    (sectors.AIRPORTS, 'Airports'),
    (
        sectors.AGRICULTURE_HORTICULTURE_AND_FISHERIES,
        'Agriculture, horticulture and fisheries'
    ),
    (sectors.AUTOMOTIVE, 'Automotive'),
    (
        sectors.BIOTECHNOLOGY_AND_PHARMACEUTICALS,
        'Biotechnology and pharmaceuticals'
    ),
    (
        sectors.BUSINESS_AND_CONSUMER_SERVICES,
        'Business and consumer services'
    ),
    (sectors.CHEMICALS, 'Chemicals'),
    (sectors.CLOTHING_FOOTWEAR_AND_FASHION, 'Clothing, footwear and fashion'),
    (sectors.COMMUNICATIONS, 'Communications'),
    (sectors.CONSTRUCTION, 'Construction'),
    (sectors.CREATIVE_AND_MEDIA, 'Creative and media'),
    (sectors.EDUCATION_AND_TRAINING, 'Education and training'),
    (sectors.ELECTRONICS_AND_IT_HARDWARE, 'Electronics and IT hardware'),
    (sectors.ENVIRONMENT, 'Environment'),
    (
        sectors.FINANCIAL_AND_PROFESSIONAL_SERVICES,
        'Financial and professional services'
    ),
    (sectors.FOOD_AND_DRINK, 'Food and drink'),
    (
        sectors.GIFTWARE_JEWELLERY_AND_TABLEWARE,
        'Giftware, jewellery and tableware'
    ),
    (sectors.GLOBAL_SPORTS_INFRASTRUCTURE, 'Global sports infrastructure'),
    (sectors.HEALTHCARE_AND_MEDICAL, 'Healthcare and medical'),
    (
        sectors.HOUSEHOLD_GOODS_FURNITURE_AND_FURNISHINGS,
        'Household goods, furniture and furnishings'
    ),
    (sectors.LIFE_SCIENCES, 'Life sciences'),
    (sectors.LEISURE_AND_TOURISM, 'Leisure and tourism'),
    (sectors.LEGAL_SERVICES, 'Legal services'),
    (sectors.MARINE, 'Marine'),
    (
        sectors.MECHANICAL_ELECTRICAL_AND_PROCESS_ENGINEERING,
        'Mechanical electrical and process engineering'
    ),
    (sectors.METALLURGICAL_PROCESS_PLANT, 'Metallurgical process plant'),
    (sectors.METALS_MINERALS_AND_MATERIALS, 'Metals, minerals and materials'),
    (sectors.MINING, 'Mining'),
    (sectors.OIL_AND_GAS, 'Oil and gas'),
    (sectors.PORTS_AND_LOGISTICS, 'Ports and logistics'),
    (sectors.POWER, 'Power'),
    (sectors.RAILWAYS, 'Railways'),
    (sectors.RENEWABLE_ENERGY, 'Renewable energy'),
    (sectors.RETAIL_AND_LUXURY, 'Retail and luxury'),
    (sectors.SECURITY, 'Security'),
    (sectors.SOFTWARE_AND_COMPUTER_SERVICES, 'Software and computer services'),
    (
        sectors.TEXTILES_INTERIOR_TEXTILES_AND_CARPETS,
        'Textiles, interior textiles and carpets'
    ),
    (sectors.WATER, 'Water'),
)

EMPLOYEES = (
    ('', 'Please select an option'),
    ('1-10', '1-10'),
    ('11-50', '11-50'),
    ('51-200', '51-200'),
    ('201-500', '201-500'),
    ('501-1000', '501-1,000'),
    ('1001-10000', '1,001-10,000'),
    ('10001+', '10,001+'),
)

CONTACT_OPTIONS = (
    ('EMAIL', 'Email'),
    ('PHONE', 'Phone'),
)

FOOD_LEAD_GENERATION_PRODUCT_TYPES = (
    ('DISCOUNT', 'Discount'),
    ('PREMIUM', 'Premium'),
)

ORDER_SIZE_OPTIONS = (
    ('1-1000', '1-1,000 items'),
    ('1000-10000', '1,000-10,000 items'),
    ('10000-100000', '10,001-100,000 items'),
    ('100000+', '100,001+ items'),
)

ORDER_DEADLINE_OPTIONS = (
    ('1-3 MONTHS', '1 to 3 months'),
    ('3-6 MONTHS', '3 to 6 months'),
    ('6-12 MONTHS', '6 months to a year'),
    ('NA', 'N/A'),
)

LEAD_GENERATION_COUNTRIES = [
    (lead_generation.FRANCE, 'France'),
    (lead_generation.SINGAPORE, 'Singapore'),
]

LEAD_GENERATION_CAMPAIGNS = [
    (lead_generation.FOOD_IS_GREAT, lead_generation.FOOD_IS_GREAT),
    (lead_generation.LEGAL_IS_GREAT, lead_generation.LEGAL_IS_GREAT),
]
