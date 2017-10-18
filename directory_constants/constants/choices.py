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

COMTRADE_SECTORS = (
    (
        'LIVE ANIMALS',
        'Live animals'
    ),
    (
        'MEAT AND EDIBLE MEAT OFFAL',
        'Meat and edible meat offal'
    ),
    (
        'FISH AND CRUSTACEANS, MOLLUSCS AND OTHER AQUATIC INVERTEBRATES',
        'Fish and crustaceans, molluscs and other aquatic invertebrates'),
    (
        'DAIRY PRODUCE; BIRDS\' EGGS; NATURAL HONEY; EDIBLE PRODUCTS OF '
        'ANIMAL ORIGIN, NOT ELSEWHERE SPECIFIED OR INCLUDED',
        'Dairy produce; birds\' eggs; natural honey; edible products of '
        'animal origin, not elsewhere specified or included'),
    (
        'PRODUCTS OF ANIMAL ORIGIN, NOT ELSEWHERE SPECIFIED OR INCLUDED',
        'Products of animal origin, not elsewhere specified or included'
    ),
    (
        'LIVE TREES AND OTHER PLANTS; BULBS, ROOTS AND THE LIKE; CUT FLOWERS '
        'AND ORNAMENTAL FOLIAGE',
        'Live trees and other plants; bulbs, roots and the like; cut flowers '
        'and ornamental foliage'
    ),
    (
        'EDIBLE VEGETABLES AND CERTAIN ROOTS AND TUBERS',
        'Edible vegetables and certain roots and tubers'
    ),
    (
        'EDIBLE FRUIT AND NUTS; PEEL OF CITRUS FRUIT OR MELONS',
        'Edible fruit and nuts; peel of citrus fruit or melons'
    ),
    (
        'COFFEE, TEA, MATé AND SPICES',
        'Coffee, tea, maté and spices'
    ),
    (
        'CEREALS',
        'Cereals'
    ),
    (
        'PRODUCTS OF THE MILLING INDUSTRY; MALT; STARCHES; INULIN; '
        'WHEAT GLUTEN',
        'Products of the milling industry; malt; starches; inulin; '
        'wheat gluten'
    ),
    (
        'OIL SEEDS AND OLEAGINOUS FRUITS; MISCELLANEOUS GRAINS,SEEDS AND FRUIT'
        '; INDUSTRIAL OR MEDICINAL PLANTS; STRAW AND FODDER',
        'Oil seeds and oleaginous fruits; miscellaneous grains,seeds and fruit'
        '; industrial or medicinal plants; straw and fodder'
    ),
    (
        'LAC; GUMS, RESINS AND OTHER VEGETABLE SAPS AND EXTRACTS',
        'Lac; gums, resins and other vegetable saps and extracts'
    ),
    (
        'VEGETABLE PLAITING MATERIALS; VEGETABLE PRODUCTS NOT ELSEWHERE '
        'SPECIFIED OR INCLUDED',
        'Vegetable plaiting materials; vegetable products not elsewhere '
        'specified or included'
    ),
    (
        'ANIMAL OR VEGETABLE FATS AND OILS AND THEIR CLEAVAGE PRODUCTS; '
        'PREPARED EDIBLE FATS; ANIMAL OR VEGETABLE WAXES',
        'Animal or vegetable fats and oils and their cleavage products; '
        'prepared edible fats; animal or vegetable waxes'
    ),
    (
        'PREPARATIONS OF MEAT, OF FISH OR OF CRUSTACEANS, MOLLUSCS OR OTHER '
        'AQUATIC INVERTEBRATES',
        'Preparations of meat, of fish or of crustaceans, molluscs or other '
        'aquatic invertebrates'
    ),
    (
        'SUGARS AND SUGAR CONFECTIONERY',
        'Sugars and sugar confectionery'
    ),
    (
        'COCOA AND COCOA PREPARATIONS',
        'Cocoa and cocoa preparations'
    ),
    (
        'PREPARATIONS OF CEREALS, FLOUR, STARCH OR MILK; '
        'PASTRYCOOKS\' PRODUCTS',
        'Preparations of cereals, flour, starch or milk; '
        'pastrycooks\' products'
    ),
    (
        'PREPARATIONS OF VEGETABLES, FRUIT, NUTS OR OTHER PARTS OF PLANTS',
        'Preparations of vegetables, fruit, nuts or other parts of plants'
    ),
    (
        'MISCELLANEOUS EDIBLE PREPARATIONS',
        'Miscellaneous edible preparations'
    ),
    (
        'BEVERAGES, SPIRITS AND VINEGAR',
        'Beverages, spirits and vinegar'
    ),
    (
        'RESIDUES AND WASTE FROM THE FOOD INDUSTRIES; PREPARED ANIMAL FODDER',
        'Residues and waste from the food industries; prepared animal fodder'
    ),
    (
        'TOBACCO AND MANUFACTURED TOBACCO SUBSTITUTES',
        'Tobacco and manufactured tobacco substitutes'
    ),
    (
        'SALT; SULPHUR; EARTHS AND STONE; '
        'PLASTERING MATERIALS, LIME AND CEMENT',
        'Salt; sulphur; earths and stone; '
        'plastering materials, lime and cement'
    ),
    (
        'ORES, SLAG AND ASH',
        'Ores, slag and ash'
    ),
    (
        'MINERAL FUELS, MINERAL OILS AND PRODUCTS OF THEIR DISTILLATION; '
        'BITUMINOUS SUBSTANCES; MINERAL WAXES',
        'Mineral fuels, mineral oils and products of their distillation; '
        'bituminous substances; mineral waxes'),
    (
        'INORGANIC CHEMICALS; ORGANIC OR INORGANIC COMPOUNDS OF PRECIOUS '
        'METALS, OF RARE-EARTH METALS, OF RADIOACTIVE ELEMENTS OR OF ISOTOPES',
        'Inorganic chemicals; organic or inorganic compounds of precious '
        'metals, of rare-earth metals, of radioactive elements or of isotopes'
    ),
    (
        'ORGANIC CHEMICALS',
        'Organic chemicals'
    ),
    (
        'PHARMACEUTICAL PRODUCTS',
        'Pharmaceutical products'
    ),
    (
        'FERTILISERS',
        'Fertilisers'
    ),
    (
        'TANNING OR DYEING EXTRACTS; TANNINS AND THEIR DERIVATIVES; '
        'DYES, PIGMENTS AND OTHER COLOURING MATTER; PAINTS AND VARNISHES; '
        'PUTTY AND OTHER MASTICS; INKS',
        'Tanning or dyeing extracts; tannins and their derivatives; '
        'dyes, pigments and other colouring matter; paints and varnishes; '
        'putty and other mastics; inks'
    ),
    (
        'ESSENTIAL OILS AND RESINOIDS; PERFUMERY, COSMETIC OR TOILET '
        'PREPARATIONS',
        'Essential oils and resinoids; perfumery, cosmetic or toilet '
        'preparations'
    ),
    (
        'SOAP, ORGANIC SURFACE-ACTIVE AGENTS, WASHING PREPARATIONS, '
        'LUBRICATING PREPARATIONS, ARTIFICIAL WAXES, PREPARED WAXES, '
        'POLISHING OR SCOURING PREPARATIONS, CANDLES AND SIMILAR ARTICLES, '
        'MODELLING PASTES, DENTAL WAXES AND DENTAL PREPARATIONS WITH A '
        'BASIS OF PLASTER',
        'Soap, organic surface-active agents, washing preparations, '
        'lubricating preparations, artificial waxes, prepared waxes, '
        'polishing or scouring preparations, candles and similar articles, '
        'modelling pastes, dental waxes and dental preparations with a '
        'basis of plaster'
    ),
    (
        'ALBUMINOIDAL SUBSTANCES; MODIFIED STARCHES; GLUES; ENZYMES',
        'Albuminoidal substances; modified starches; glues; enzymes'
    ),
    (
        'EXPLOSIVES; PYROTECHNIC PRODUCTS; MATCHES; PYROPHORIC ALLOYS; '
        'CERTAIN COMBUSTIBLE PREPARATIONS',
        'Explosives; pyrotechnic products; matches; pyrophoric alloys; '
        'certain combustible preparations'
    ),
    (
        'PHOTOGRAPHIC OR CINEMATOGRAPHIC GOODS',
        'Photographic or cinematographic goods'
    ),
    (
        'MISCELLANEOUS CHEMICAL PRODUCTS',
        'Miscellaneous chemical products'
    ),
    (
        'PLASTICS AND ARTICLES THEREOF',
        'Plastics and articles thereof'
    ),
    (
        'RUBBER AND ARTICLES THEREOF',
        'Rubber and articles thereof'
    ),
    (
        'RAW HIDES AND SKINS (OTHER THAN FURSKINS) AND LEATHER',
        'Raw hides and skins (other than furskins) and leather'
    ),
    (
        'ARTICLES OF LEATHER; SADDLERY AND HARNESS; TRAVEL GOODS, '
        'HANDBAGS AND SIMILAR CONTAINERS; ARTICLES OF ANIMAL GUT '
        '(OTHER THAN SILK-WORM GUT)',
        'Articles of leather; saddlery and harness; travel goods, '
        'handbags and similar containers; articles of animal gut '
        '(other than silk-worm gut)'
    ),
    (
        'FURSKINS AND ARTIFICIAL FUR; MANUFACTURES THEREOF',
        'Furskins and artificial fur; manufactures thereof'
    ),
    (
        'WOOD AND ARTICLES OF WOOD; WOOD CHARCOAL',
        'Wood and articles of wood; wood charcoal'
    ),
    (
        'CORK AND ARTICLES OF CORK',
        'Cork and articles of cork'
    ),
    (
        'MANUFACTURES OF STRAW, OF ESPARTO OR OF OTHER PLAITING MATERIALS; '
        'BASKETWARE AND WICKERWORK',
        'Manufactures of straw, of esparto or of other plaiting materials; '
        'basketware and wickerwork'
    ),
    (
        'PULP OF WOOD OR OF OTHER FIBROUS CELLULOSIC MATERIAL; RECOVERED '
        '(WASTE AND SCRAP) PAPER OR PAPERBOARD',
        'Pulp of wood or of other fibrous cellulosic material; recovered '
        '(waste and scrap) paper or paperboard'
    ),
    (
        'PAPER AND PAPERBOARD; ARTICLES OF PAPER PULP, OF PAPER OR OF '
        'PAPERBOARD',
        'Paper and paperboard; articles of paper pulp, of paper or of '
        'paperboard'
    ),
    (
        'PRINTED BOOKS, NEWSPAPERS, PICTURES AND OTHER PRODUCTS OF '
        'THE PRINTING INDUSTRY; MANUSCRIPTS, TYPESCRIPTS AND PLANS',
        'Printed books, newspapers, pictures and other products of '
        'the printing industry; manuscripts, typescripts and plans'
    ),
    (
        'SILK',
        'Silk'
    ),
    (
        'WOOL, FINE OR COARSE ANIMAL HAIR; HORSEHAIR YARN AND WOVEN FABRIC',
        'Wool, fine or coarse animal hair; horsehair yarn and woven fabric'
    ),
    (
        'COTTON',
        'Cotton'
    ),
    (
        'OTHER VEGETABLE TEXTILE FIBRES; PAPER YARN AND WOVEN FABRICS '
        'OF PAPER YARN',
        'Other vegetable textile fibres; paper yarn and woven fabrics '
        'of paper yarn'
    ),
    (
        'MAN-MADE FILAMENTS; STRIP AND THE LIKE OF MAN-MADE TEXTILE MATERIALS',
        'Man-made filaments; strip and the like of man-made textile materials'
    ),
    (
        'MAN-MADE STAPLE FIBRES',
        'Man-made staple fibres'
    ),
    (
        'WADDING, FELT AND NONWOVENS; SPECIAL YARNS; TWINE, CORDAGE, '
        'ROPES AND CABLES AND ARTICLES THEREOF',
        'Wadding, felt and nonwovens; special yarns; twine, cordage, '
        'ropes and cables and articles thereof'
    ),
    (
        'CARPETS AND OTHER TEXTILE FLOOR COVERINGS',
        'Carpets and other textile floor coverings'
    ),
    (
        'SPECIAL WOVEN FABRICS; TUFTED TEXTILE FABRICS; LACE; TAPESTRIES; '
        'TRIMMINGS; EMBROIDERY',
        'Special woven fabrics; tufted textile fabrics; lace; tapestries; '
        'trimmings; embroidery'
    ),
    (
        'IMPREGNATED, COATED, COVERED OR LAMINATED TEXTILE FABRICS; '
        'TEXTILE ARTICLES OF A KIND SUITABLE FOR INDUSTRIAL USE',
        'Impregnated, coated, covered or laminated textile fabrics; '
        'textile articles of a kind suitable for industrial use'
    ),
    (
        'KNITTED OR CROCHETED FABRICS',
        'Knitted or crocheted fabrics'
    ),
    (
        'ARTICLES OF APPAREL AND CLOTHING ACCESSORIES, KNITTED OR CROCHETED',
        'Articles of apparel and clothing accessories, knitted or crocheted'
    ),
    (
        'ARTICLES OF APPAREL AND CLOTHING ACCESSORIES,NOT KNITTED OR '
        'CROCHETED',
        'Articles of apparel and clothing accessories,not knitted or '
        'crocheted'
    ),
    (
        'OTHER MADE UP TEXTILE ARTICLES; SETS; WORN CLOTHING AND '
        'WORN TEXTILE ARTICLES; RAGS',
        'Other made up textile articles; sets; worn clothing and '
        'worn textile articles; rags'
    ),
    (
        'FOOTWEAR, GAITERS AND THE LIKE; PARTS OF SUCH ARTICLES',
        'Footwear, gaiters and the like; parts of such articles'
    ),
    (
        'HEADGEAR AND PARTS THEREOF',
        'Headgear and parts thereof'
    ),
    (
        'UMBRELLAS, SUN UMBRELLAS, WALKING-STICKS, SEAT-STICKS, WHIPS, '
        'RIDING-CROPS AND PARTS THEREOF',
        'Umbrellas, sun umbrellas, walking-sticks, seat-sticks, whips, '
        'riding-crops and parts thereof'
    ),
    (
        'PREPARED FEATHERS AND DOWN AND ARTICLES MADE OF FEATHERS OR OF DOWN; '
        'ARTIFICIAL FLOWERS; ARTICLES OF HUMAN HAIR',
        'Prepared feathers and down and articles made of feathers or of down; '
        'artificial flowers; articles of human hair'
    ),
    (
        'ARTICLES OF STONE, PLASTER, CEMENT, ASBESTOS, '
        'MICA OR SIMILAR MATERIALS',
        'Articles of stone, plaster, cement, asbestos, '
        'mica or similar materials'
    ),
    (
        'CERAMIC PRODUCTS',
        'Ceramic products'
    ),
    (
        'GLASS AND GLASSWARE',
        'Glass and glassware'
    ),
    (
        'NATURAL OR CULTURED PEARLS, PRECIOUS OR SEMI-PRECIOUS STONES, '
        'PRECIOUS METALS, METALS CLAD WITH PRECIOUS METAL, AND ARTICLES '
        'THEREOF; IMITATION JEWELLERY; COIN',
        'Natural or cultured pearls, precious or semi-precious stones, '
        'precious metals, metals clad with precious metal, and articles '
        'thereof; imitation jewellery; coin'
    ),
    (
        'IRON AND STEEL',
        'Iron and steel'
    ),
    (
        'ARTICLES OF IRON OR STEEL',
        'Articles of iron or steel'
    ),
    (
        'COPPER AND ARTICLES THEREOF',
        'Copper and articles thereof'
    ),
    (
        'NICKEL AND ARTICLES THEREOF',
        'Nickel and articles thereof'
    ),
    (
        'ALUMINIUM AND ARTICLES THEREOF',
        'Aluminium and articles thereof'
    ),
    (
        'LEAD AND ARTICLES THEREOF',
        'Lead and articles thereof'
    ),
    (
        'ZINC AND ARTICLES THEREOF',
        'Zinc and articles thereof'
    ),
    (
        'TIN AND ARTICLES THEREOF',
        'Tin and articles thereof'
    ),
    (
        'OTHER BASE METALS; CERMETS; ARTICLES THEREOF',
        'Other base metals; cermets; articles thereof'
    ),
    (
        'TOOLS, IMPLEMENTS, CUTLERY, SPOONS AND FORKS, OF BASE METAL; '
        'PARTS THEREOF OF BASE METAL',
        'Tools, implements, cutlery, spoons and forks, of base metal; '
        'parts thereof of base metal'
    ),
    (
        'MISCELLANEOUS ARTICLES OF BASE METAL',
        'Miscellaneous articles of base metal'
    ),
    (
        'NUCLEAR REACTORS, BOILERS, MACHINERY AND MECHANICAL APPLIANCES; '
        'PARTS THEREOF',
        'Nuclear reactors, boilers, machinery and mechanical appliances; '
        'parts thereof'
    ),
    (
        'ELECTRICAL MACHINERY AND EQUIPMENT AND PARTS THEREOF; '
        'SOUND RECORDERS AND REPRODUCERS, TELEVISION IMAGE AND SOUND '
        'RECORDERS AND REPRODUCERS, AND PARTS AND ACCESSORIES OF SUCH '
        'ARTICLES',
        'Electrical machinery and equipment and parts thereof; '
        'sound recorders and reproducers, television image and sound '
        'recorders and reproducers, and parts and accessories of such '
        'articles'
    ),
    (
        'RAILWAY OR TRAMWAY LOCOMOTIVES, ROLLING-STOCK AND PARTS THEREOF; '
        'RAILWAY OR TRAMWAY TRACK FIXTURES AND FITTINGS AND PARTS THEREOF; '
        'MECHANICAL (INCLUDING ELECTRO-MECHANICAL) TRAFFIC SIGNALLING '
        'EQUIPMENT OF ALL KINDS',
        'Railway or tramway locomotives, rolling-stock and parts thereof; '
        'railway or tramway track fixtures and fittings and parts thereof; '
        'mechanical (including electro-mechanical) traffic signalling '
        'equipment of all kinds'
    ),
    (
        'VEHICLES OTHER THAN RAILWAY OR TRAMWAY ROLLING-STOCK, AND PARTS '
        'AND ACCESSORIES THEREOF',
        'Vehicles other than railway or tramway rolling-stock, and parts '
        'and accessories thereof'
    ),
    (
        'AIRCRAFT, SPACECRAFT, AND PARTS THEREOF',
        'Aircraft, spacecraft, and parts thereof'
    ),
    (
        'SHIPS, BOATS AND FLOATING STRUCTURES',
        'Ships, boats and floating structures'
    ),
    (
        'OPTICAL, PHOTOGRAPHIC, CINEMATOGRAPHIC, MEASURING, CHECKING, '
        'PRECISION, MEDICAL OR SURGICAL INSTRUMENTS AND APPARATUS; PARTS '
        'AND ACCESSORIES THEREOF',
        'Optical, photographic, cinematographic, measuring, checking, '
        'precision, medical or surgical instruments and apparatus; parts '
        'and accessories thereof'
    ),
    (
        'CLOCKS AND WATCHES AND PARTS THEREOF',
        'Clocks and watches and parts thereof'
    ),
    (
        'MUSICAL INSTRUMENTS; PARTS AND ACCESSORIES OF SUCH ARTICLES',
        'Musical instruments; parts and accessories of such articles'
    ),
    (
        'ARMS AND AMMUNITION; PARTS AND ACCESSORIES THEREOF',
        'Arms and ammunition; parts and accessories thereof'
    ),
    (
        'FURNITURE; BEDDING, MATTRESSES, MATTRESS SUPPORTS, CUSHIONS AND '
        'SIMILAR STUFFED FURNISHINGS; LAMPS AND LIGHTING FITTINGS, NOT '
        'ELSEWHERE SPECIFIED OR INCLUDED; ILLUMINATED SIGNS, ILLUMINATED '
        'NAME-PLATES AND THE LIKE; PREFABRICATED BUILDINGS',
        'Furniture; bedding, mattresses, mattress supports, cushions and '
        'similar stuffed furnishings; lamps and lighting fittings, not '
        'elsewhere specified or included; illuminated signs, illuminated '
        'name-plates and the like; prefabricated buildings'
    ),
    (
        'TOYS, GAMES AND SPORTS REQUISITES; PARTS AND ACCESSORIES THEREOF',
        'Toys, games and sports requisites; parts and accessories thereof'
    ),
    (
        'MISCELLANEOUS MANUFACTURED ARTICLES',
        'Miscellaneous manufactured articles'
    ),
    (
        'WORKS OF ART, COLLECTORS\' PIECES AND ANTIQUES',
        'Works of art, collectors\' pieces and antiques'
    ),
    (
        'COMMODITIES NOT SPECIFIED ACCORDING TO KIND',
        'Commodities not specified according to kind'
    ),
)
