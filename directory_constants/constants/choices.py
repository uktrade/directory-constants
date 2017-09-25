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
BUSINESS_MODELS = (
    (DISTRIBUTION, 'Distribution'),
    (WHOLESALE, 'Wholesale'),
    (RETAIL, 'Retail'),
)
SUBSECTOR_SELECTION = (
    (RETAIL, 'Retail'),
    (HOSPITALITY, 'Hospitality'),
    (CATERING, 'Catering'),
    (MANUFACTURING, 'Manufacturing'),
)
EXPORT_DESTINATIONS = (
    ('CN', 'China'),
    ('DE', 'Germany'),
    ('IN', 'India'),
    ('JP', 'Japan'),
    ('US', 'United States'),
)
INDUSTRIES = (
    ('AEROSPACE', 'Aerospace'),
    (
        'AGRICULTURE_HORTICULTURE_AND_FISHERIES',
        'Agriculture, horticulture and fisheries'
    ),
    ('AIRPORTS', 'Airports'),
    ('AUTOMOTIVE', 'Automotive'),
    ('BIOTECHNOLOGY_AND_PHARMACEUTICALS', 'Biotechnology and pharmaceuticals'),
    ('BUSINESS_AND_CONSUMER_SERVICES', 'Business and consumer services'),
    ('CHEMICALS', 'Chemicals'),
    ('CLOTHING_FOOTWEAR_AND_FASHION', 'Clothing, footwear and fashion'),
    ('COMMUNICATIONS', 'Communications'),
    ('CONSTRUCTION', 'Construction'),
    ('CREATIVE_AND_MEDIA', 'Creative and media'),
    ('EDUCATION_AND_TRAINING', 'Education and training'),
    ('ELECTRONICS_AND_IT_HARDWARE', 'Electronics and IT hardware'),
    ('ENVIRONMENT', 'Environment'),
    (
        'FINANCIAL_AND_PROFESSIONAL_SERVICES',
        'Financial and professional services'
    ),
    ('FOOD_AND_DRINK', 'Food and drink'),
    ('GIFTWARE_JEWELLERY_AND_TABLEWARE', 'Giftware, jewellery and tableware'),
    ('GLOBAL_SPORTS_INFRASTRUCTURE', 'Global sports infrastructure'),
    ('HEALTHCARE_AND_MEDICAL', 'Healthcare and medical'),
    (
        'HOUSEHOLD_GOODS_FURNITURE_AND_FURNISHINGS',
        'Household goods, furniture and furnishings'
    ),
    ('LEISURE_AND_TOURISM', 'Leisure and tourism'),
    ('LEGAL_SERVICES', 'Legal services'),
    ('MARINE', 'Marine'),
    (
        'MECHANICAL_ELECTRICAL_AND_PROCESS_ENGINEERING',
        'Mechanical electrical and process engineering'
    ),
    ('METALLURGICAL_PROCESS_PLANT', 'Metallurgical process plant'),
    ('METALS_MINERALS_AND_MATERIALS', 'Metals, minerals and materials'),
    ('MINING', 'Mining'),
    ('OIL_AND_GAS', 'Oil and gas'),
    ('PORTS_AND_LOGISTICS', 'Ports and logistics'),
    ('POWER', 'Power'),
    ('RAILWAYS', 'Railways'),
    ('RENEWABLE_ENERGY', 'Renewable energy'),
    ('RETAIL_AND_LUXURY', 'Retail and luxury'),
    ('SECURITY', 'Security'),
    ('SOFTWARE_AND_COMPUTER_SERVICES', 'Software and computer services'),
    (
        'TEXTILES_INTERIOR_TEXTILES_AND_CARPETS',
        'Textiles, interior textiles and carpets'
    ),
    ('WATER', 'Water'),
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

PRODUCT_TYPE_OPTIONS = (
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

LEAD_GENERATION_COUNTRIES = ['france', 'singapore']
LEAD_GENERATION_CAMPAIGNS = ['food-is-great']
