from collections import OrderedDict

CODES_SECTORS_DICT = OrderedDict([
    # goods
    ('HS01', 'Animals; live'),
    ('HS02', 'Meat and edible meat offal'),
    ('HS03', 'Fish and crustaceans, molluscs and other aquatic invertebrates'),
    ('HS04', 'Dairy produce; birds\' eggs; natural honey; edible products of '
             'animal origin, not elsewhere specified or included'),
    ('HS05', 'Animal originated products; not elsewhere specified or '
             'included'),
    ('HS06', 'Trees and other plants, live; bulbs, roots and the like; cut '
             'flowers and ornamental foliage'),
    ('HS07', 'Vegetables and certain roots and tubers; edible'),
    ('HS08', 'Fruit and nuts, edible; peel of citrus fruit or melons'),
    ('HS09', 'Coffee, tea, mate and spices'),
    ('HS10', 'Cereals'),
    ('HS11', 'Products of the milling industry; malt, starches, inulin, '
             'wheat gluten'),
    ('HS12', 'Oil seeds and oleaginous fruits; miscellaneous grains, seeds '
             'and fruit, industrial or medicinal plants; straw and fodder'),
    ('HS13', 'Lac; gums, resins and other vegetable saps and extracts'),
    ('HS14', 'Vegetable plaiting materials; vegetable products not elsewhere '
             'specified or included'),
    ('HS15', 'Animal or vegetable fats and oils and their cleavage products; '
             'prepared animal fats; animal or vegetable waxes'),
    ('HS16', 'Meat, fish or crustaceans, molluscs or other aquatic '
             'invertebrates; preparations thereof'),
    ('HS17', 'Sugars and sugar confectionery'),
    ('HS18', 'Cocoa and cocoa preparations'),
    ('HS19', 'Preparations of cereals, flour, starch or milk; '
             'pastrycooks\' products'),
    ('HS20', 'Preparations of vegetables, fruit, nuts or other parts of '
             'plants'),
    ('HS21', 'Miscellaneous edible preparations'),
    ('HS22', 'Beverages, spirits and vinegar'),
    ('HS23', 'Food industries, residues and wastes thereof; prepared '
             'animal fodder'),
    ('HS24', 'Tobacco and manufactured tobacco substitutes'),
    ('HS25', 'Salt; sulphur; earths, stone; plastering materials, '
             'lime and cement'),
    ('HS26', 'Ores, slag and ash'),
    ('HS27', 'Mineral fuels, mineral oils and products of their distillation; '
             'bituminous substances; mineral waxes'),
    ('HS28', 'Inorganic chemicals; organic and inorganic compounds of '
             'precious metals; of rare earth metals, of radio-active elements '
             'and of isotopes'),
    ('HS29', 'Organic chemicals'),
    ('HS30', 'Pharmaceutical products'),
    ('HS31', 'Fertilizers'),
    ('HS32', 'Tanning or dyeing extracts; tannins and their derivatives; '
             'dyes, pigments and other colouring matter; paints, varnishes; '
             'putty, other mastics; inks'),
    ('HS33', 'Essential oils and resinoids; perfumery, cosmetic or toilet '
             'preparations'),
    ('HS34', 'Soap, organic surface-active agents; washing, lubricating, '
             'polishing or scouring preparations; artificial or prepared '
             'waxes, candles and similar articles, modelling pastes, dental '
             'waxes and dental preparations with a basis of plaster'),
    ('HS35', 'Albuminoidal substances; modified starches; glues; enzymes'),
    ('HS36', 'Explosives; pyrotechnic products; matches; pyrophoric alloys; '
             'certain combustible preparations'),
    ('HS37', 'Photographic or cinematographic goods'),
    ('HS38', 'Chemical products n.e.c.'),
    ('HS39', 'Plastics and articles thereof'),
    ('HS40', 'Rubber and articles thereof'),
    ('HS41', 'Raw hides and skins (other than furskins) and leather'),
    ('HS42', 'Articles of leather; saddlery and harness; travel goods, '
             'handbags and similar containers; articles of animal gut '
             '(other than silk-worm gut)'),
    ('HS43', 'Furskins and artificial fur; manufactures thereof'),
    ('HS44', 'Wood and articles of wood; wood charcoal'),
    ('HS45', 'Cork and articles of cork'),
    ('HS46', 'Manufactures of straw, esparto or other plaiting materials; '
             'basketware and wickerwork'),
    ('HS47', 'Pulp of wood or other fibrous cellulosic material; recovered '
             '(waste and scrap) paper or paperboard'),
    ('HS48', 'Paper and paperboard; articles of paper pulp, of paper or '
             'paperboard'),
    ('HS49', 'Printed books, newspapers, pictures and other products of the '
             'printing industry; manuscripts, typescripts and plans'),
    ('HS50', 'Silk'),
    ('HS51', 'Wool, fine or coarse animal hair; horsehair yarn and woven '
             'fabric'),
    ('HS52', 'Cotton'),
    ('HS53', 'Vegetable textile fibres; paper yarn and woven fabrics of '
             'paper yarn'),
    ('HS54', 'Man-made filaments; strip and the like of man-made textile '
             'materials'),
    ('HS55', 'Man-made staple fibres'),
    ('HS56', 'Wadding, felt and nonwovens, special yarns; twine, cordage, '
             'ropes and cables and articles thereof'),
    ('HS57', 'Carpets and other textile floor coverings'),
    ('HS58', 'Fabrics; special woven fabrics, tufted textile fabrics, lace, '
             'tapestries, trimmings, embroidery'),
    ('HS59', 'Textile fabrics; impregnated, coated, covered or laminated; '
             'textile articles of a kind suitable for industrial use'),
    ('HS60', 'Fabrics; knitted or crocheted'),
    ('HS61', 'Apparel and clothing accessories; knitted or crocheted'),
    ('HS62', 'Apparel and clothing accessories; not knitted or crocheted'),
    ('HS63', 'Textiles, made up articles; sets; worn clothing and worn '
             'textile articles; rags'),
    ('HS64', 'Footwear; gaiters and the like; parts of such articles'),
    ('HS65', 'Headgear and parts thereof'),
    ('HS66', 'Umbrellas, sun umbrellas, walking-sticks, seat sticks, whips, '
             'riding crops; and parts thereof'),
    ('HS67', 'Feathers and down, prepared; and articles made of feather or '
             'of down; artificial flowers; articles of human hair'),
    ('HS68', 'Stone, plaster, cement, asbestos, mica or similar materials; '
             'articles thereof'),
    ('HS69', 'Ceramic products'),
    ('HS70', 'Glass and glassware'),
    ('HS71', 'Natural, cultured pearls; precious, semi-precious stones; '
             'precious metals, metals clad with precious metal, '
             'and articles thereof; imitation jewellery; coin'),
    ('HS72', 'Iron and steel'),
    ('HS73', 'Iron or steel articles'),
    ('HS74', 'Copper and articles thereof'),
    ('HS75', 'Nickel and articles thereof'),
    ('HS76', 'Aluminium and articles thereof'),
    ('HS78', 'Lead and articles thereof'),
    ('HS79', 'Zinc and articles thereof'),
    ('HS80', 'Tin; articles thereof'),
    ('HS81', 'Metals; n.e.c., cermets and articles thereof'),
    ('HS82', 'Tools, implements, cutlery, spoons and forks, of base metal; '
             'parts thereof, of base metal'),
    ('HS83', 'Metal; miscellaneous products of base metal'),
    ('HS84', 'Nuclear reactors, boilers, machinery and mechanical appliances; '
             'parts thereof'),
    ('HS85', 'Electrical machinery and equipment and parts thereof; sound '
             'recorders and reproducers; television image and sound recorders '
             'and reproducers, parts and accessories of such articles'),
    ('HS86', 'Railway, tramway locomotives, rolling-stock and parts thereof; '
             'railway or tramway track fixtures and fittings and parts '
             'thereof; mechanical (including electro-mechanical) traffic '
             'signalling equipment of all kinds'),
    ('HS87', 'Vehicles; other than railway or tramway rolling stock, and '
             'parts and accessories thereof'),
    ('HS88', 'Aircraft, spacecraft and parts thereof'),
    ('HS89', 'Ships, boats and floating structures'),
    ('HS90', 'Optical, photographic, cinematographic, measuring, checking, '
             'medical or surgical instruments and apparatus; parts and '
             'accessories'),
    ('HS91', 'Clocks and watches and parts thereof'),
    ('HS92', 'Musical instruments; parts and accessories of such articles'),
    ('HS94', 'Furniture; bedding, mattresses, mattress supports, cushions and '
             'similar stuffed furnishings; lamps and lighting fittings, '
             'n.e.c.; illuminated signs, illuminated name-plates and the '
             'like; prefabricated buildings'),
    ('HS95', 'Toys, games and sports requisites; parts and accessories '
             'thereof'),
    ('HS96', 'Miscellaneous manufactured articles'),
    ('HS97', 'Works of art; collectors\' pieces and antiques'),
    ('HS99', 'Commodities not specified according to kind'),
    # services
    ('EB1', 'Transportation'),
    ('EB2', 'Travel'),
    ('EB3', 'Communications services'),
    ('EB4', 'Construction services'),
    ('EB5', 'Insurance services'),
    ('EB6', 'Financial services'),
    ('EB7', 'Computer and information services'),
    ('EB8', 'Royalties and license fees'),
    ('EB9', 'Other business services'),
    ('EB10', 'Personal, cultural, and recreational services'),
    ('EB11', 'Government services, n.i.e.'),
])


SECTORS_CHOICES = tuple(CODES_SECTORS_DICT.items())
