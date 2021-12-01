BEGIN;


INSERT INTO pr_zh.t_river_basin VALUES
(1, 'bassin versant 1', '0103000020E610000001000000110000005B0A48FB1F80044071C971A774824640427C60C77F010540CF656A12BC874640779D0DF9674605400874266DAA884640A54FABE80FAD05405B971AA19F854640315D88D51F61054061360186E581464083BEF4F6E7020540CFD90242EB7D464010CCD1E3F7B60440B39597FC4F7A4640255CC823B8510440A20E2BDCF2774640EC1516DC0F180440E388B5F814764640B7B3AF3C48EF0340C6FD47A643774640C03C64CA87A00340D15CA79196744640077DE9EDCF850340501729948575464083DE1B4300B003409F1D705D31794640B6679604A8E90340594C6C3EAE7B4640A86DC328083E044042CC2555DB7D46409F71E1404876044081CCCEA2778046405B0A48FB1F80044071C971A774824640', 604, 603),
(2, 'bassin versant 2', '0103000020E6100000010000000D000000B2D47ABFD1AE0540C1AA7AF99D86464065A71FD4454A05404DD9E90775894640DA722EC555850540990D32C9C88B4640AA99B514909605405A828C800A914640228AC91B60C60540FF5C34643C9E4640FFB3E6C75F7A06402BF9D85DA09C4640F6B704E09FB206405B25581CCE964640FDDAFAE93F8B0640E222F77475934640F0E0270EA0DF0640BC7669C3618D46408736001B106106409FABADD85F8E4640126BF12900260640359A5C8C818D46409D2CB5DE6FD40540A9143B1A878A4640B2D47ABFD1AE0540C1AA7AF99D864640', 608, 598),
(3, 'bassin versant 3', '0103000020E610000001000000140000005E0F26C5C7C70540060DFD135C9E46402AADBF25009F0540105A0F5F269A4640E86A2BF6979D054097E315889E9646402EABB019E0820540A5164A26A79246406D5512D9077905405303CDE7DC8F4640779D0DF967460540381092054C904640800C1D3BA8240540A583F57F0E8F46403D7E6FD39F1D054031074147AB9046403DF19C2D20340540D34CF73AA9914640D1AE42CA4FAA04402F6EA301BC974640ADF886C2670B0440616BB6F2929B46407923F3C81FCC03404D81CCCEA29B464050E27327D85F0340FF5C34643C9E4640F25F20089001044025CD1FD3DA9E46406552431B804D044064B14D2A1A9F4640E0F42EDE8F5B04405854C4E924A146407FC00303081F0540E9F351465CA44640B39597FC4F5E054040FB912232A246402AADBF25009F05400A100533A6A046405E0F26C5C7C70540060DFD135C9E4640', 607, 599)
;


INSERT INTO pr_zh.t_hydro_area VALUES
(1, 'zone hydro 1', '0103000020E610000001000000090000009C16BCE82B2805408202EFE4D3874640B89388F02F420540CFF6E80DF7854640713D0AD7A3B004401A868F88297F46408EC9E2FE2313044041F4A44C6A7846403B527DE717C5034088F37002D3774640786000E143890440058A58C4B07F464015CAC2D7D79A044061360186E581464045A165DD3FF604400EA14ACD1E8646409C16BCE82B2805408202EFE4D3874640'),
(2, 'zone hydro 2', '0103000020E6100000010000000B000000AD4B8DD0CF7405408B8862F20686464048DC63E9439705405FEE93A300854640757808E3A7510540D4282499D581464059FB3BDBA337054062DBA2CC068146402499D53BDC0E05404E29AF95D07F46408908FF2268EC04403FADA23F347D4640354580D3BB9804407A1C06F3577A4640AB92C83EC83204406FD8B628B37746404AEB6F09C0DF0440A9A5B915C27E464059FB3BDBA3370540D5CA845FEA834640AD4B8DD0CF7405408B8862F206864640'),
(3, 'zone hydro 3', '0103000020E61000000100000005000000F1660DDE576505402BA5677A89914640A1D79FC4E74E0440170FEF39B09C464061545227A0690440FF5C34643C9E4640B56E83DA6F4D0540EBC726F911954640F1660DDE576505402BA5677A89914640'),
(4, 'zone hydro 4', '0103000020E61000000100000006000000AF97A608707A0540CE380D518593464031D0B52FA0770540AAB706B64A984640C58D5BCCCFED04405854C4E924A14640143DF03158B10440E7C589AF76A04640FD87F4DBD7210540C91EA16648994640AF97A608707A0540CE380D5185934640'),
(5, 'zone hydro 5', '0103000020E61000000100000007000000E86A2BF6979D054048179B560A9F464079E92631084C05405854C4E924A146401A51DA1B7C4105404D8237A4519F46400B0BEE073C900540C3D7D7BAD49A464022179CC1DFAF05407ADFF8DA339B46406380441328C205400EDC813AE59D4640E86A2BF6979D054048179B560A9F4640'),
(6, 'zone hydro 6', '0103000020E610000001000000080000009A07B0C8AFDF05400F5F268A909C4640E5B8533A58BF0540EE3F321D3A9146404EF04DD367270640A5164A26A7924640C90567F0F74B06403AC9569753944640C1E270E657730640CEDF844204944640C1559E40D88906400B7DB08C0D97464042CF66D5E76A06409B030473F49A46409A07B0C8AFDF05400F5F268A909C4640'),
(7, 'zone hydro 7', '0103000020E6100000010000000B00000084D4EDEC2BAF0540F9BEB854A58F46402861A6ED5F990540F7031E18408E464089450C3B8CA90540E50E9BC8CC8B464030849CF7FF71054038656EBE11894640A774B0FECFA1054039D0436D1B884640B3D2A414741B06405C3D27BD6F8E46405F984C158C8A06409E7AA4C16D8F4640569C6A2DCCC20640B6813B50A78E46405DBF60376C9B064027124C35B39046402254A9D9036D0640D7DF12807F92464084D4EDEC2BAF0540F9BEB854A58F4640')
;


INSERT INTO pr_zh.t_fct_area VALUES
(1, '0103000020E610000001000000050000009F776341611006406AD95A5F249A464080D591239D010640F29881CAF8994640663046240A0D0640B4ACFBC742984640E54350357A1506406FBDA607059946409F776341611006406AD95A5F249A4640'),
(2, '0103000020E6100000010000000500000031992A18955406406FBDA60705994640E98024ECDB49064044C2F7FE069946405439ED293947064039454772F9974640EF5696E82C5306400E863AAC7097464031992A18955406406FBDA60705994640')
;


INSERT INTO pr_zh.t_references(authors,pub_year,title,editor,editor_location) VALUES
('Hamouda A', 2021, 'la zone humide en front pour les nuls', 'NS', 'Marseille'),
('Corny J', 2020, 'les MCD de zones humides', 'bla bla editeurs', 'quelque part'),
('Jambon A', 2021, 'comment créer sa zone humide chez soi', 'editor', 'par là')
;



-- insert into t_nomenclature Calavon river basin rules as an example for hierarchy

INSERT INTO ref_nomenclatures.t_nomenclatures(id_type, cd_nomenclature, mnemonique, label_default, label_fr, source, statut) VALUES
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'iso', 'ZH isolée', 'ZH isolée', 'ZH isolée', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'res', 'ZH participant d''un réseau ou continuum', 'ZH participant d''un réseau ou continuum', 'ZH participant d''un réseau ou continuum', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '0', 'Aucun', 'Aucun', 'Aucun', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '1 ou 2', '1 ou 2', '1 ou 2', '1 ou 2', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '2 à 5', '2 à 5', '2 à 5', '2 à 5', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '>5', '>5', '>5', '>5', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '1 à 4', '1 à 4', '1 à 4', '1 à 4', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '5 à 7', '5 à 7', '5 à 7', '5 à 7', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '8 ou 9', '8 ou 9', '8 ou 9', '8 ou 9', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '>9', '>9', '>9', '>9', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '1', '1', '1', '1', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '2', '2', '2', '2', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '3', '3', '3', '3', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), '>3', '>3', '>3', '>3', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'faible', 'Faible (conventionnel / contractuel / inventaire)', 'Faible (conventionnel / contractuel / inventaire)', 'Faible (conventionnel / contractuel / inventaire)', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'fort', 'Fort (réglementaire / maîtrise foncière)', 'Fort (réglementaire / maîtrise foncière)', 'Fort (réglementaire / maîtrise foncière)', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'OUI', 'OUI', 'OUI', 'OUI', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'NON', 'NON', 'NON', 'NON', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'bon', 'Non dégradée (bon)', 'Non dégradée (bon)', 'Non dégradée (bon)', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'mauvais', 'Très fortement dégradée (mauvais)', 'Très fortement dégradée (mauvais)', 'Très fortement dégradée (mauvais)', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'moyen', 'Partiellement dégradée (moyen)', 'Partiellement dégradée (moyen)', 'Partiellement dégradée (moyen)', 'ZONES_HUMIDES', 'Non validé'),
((SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY'), 'NE', 'Non évalué', 'Non évalué', 'Non évalué', 'ZONES_HUMIDES', 'Non validé')
;


-- example with bassin versant du calavon (here rb_id = 1) :

INSERT INTO pr_zh.cor_rb_rules VALUES
(1, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 1),
(2, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 2),
(3, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 3),
(4, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 4),
(5, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 5),
(6, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 6),
(7, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 7),
(8, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 8),
(9, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 9),
(10, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 10),
(11, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 11),
(12, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 12),
(13, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 13),
(14, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 14),
(15, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 15),
(16, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 1'), 16),
(17, (SELECT id_rb FROM pr_zh.t_river_basin WHERE name = 'bassin versant 2'), 1)
;


-- to do : mettre check val max 100 pour note ?
INSERT INTO pr_zh.t_items VALUES
(1, 1, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = '07 - zones humides de bas fonds en tête de bassin'), 100, 1),
(2, 1, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = '11 - zones humides ponctuelles'), 75, 1),
(3, 1, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = '05 - bordures de cours d''eau'), 50, 1),
(4, 1, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = '06 - plaines alluviales'), 25, 1),
(5, 1, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = '13 - zones humides artificielles'), 0, 1),

(6, 2, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 2),
(7, 2, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 1, 3),
(8, 2, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1 ou 2' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 13, 2),
(9, 2, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1 ou 2' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 13, 3),
(10, 2, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '2 à 5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 19, 2),
(11, 2, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '2 à 5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 19, 3),
(12, 2, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 25, 2),
(13, 2, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 25, 3),

(14, 3, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 2),
(15, 3, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 1, 3),
(16, 3, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1 ou 2' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 11, 2),
(17, 3, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1 ou 2' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 14, 3),
(18, 3, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '2 à 5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 17, 2),
(19, 3, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '2 à 5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 19, 3),
(20, 3, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 22, 2),
(21, 3, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 25, 3),

(22, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 2),
(23, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 1, 3),
(24, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1 à 4' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 9, 2),
(25, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1 à 4' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 11, 3),
(26, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '5 à 7' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 14, 2),
(27, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '5 à 7' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 16, 3),
(28, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '8 ou 9' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 18, 2),
(29, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '8 ou 9' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 20, 3),
(30, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>9' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 23, 2),
(31, 4, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>9' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 25, 3),

(32, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 2),
(33, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 1, 3),
(34, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 9, 2),
(35, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 11, 3),
(36, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '2' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 14, 2),
(37, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '2' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 16, 3),
(38, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '3' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 18, 2),
(39, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '3' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 20, 3),
(40, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>3' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 23, 2),
(41, 5, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>3' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 25, 3),

-- a inserer avec trigger quand 6 inséré dans cor_rb_rules
(42, 6, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'ZH isolée' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 1),
(43, 6, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'ZH participant d''un réseau ou continuum' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 100, 1),

(44, 7, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 15, 2),
(45, 7, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 15, 3),
(46, 7, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Nulle à faible'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 0, 2),
(47, 7, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Nulle à faible'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 10, 3),
(48, 7, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Moyenne'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 20, 2),
(49, 7, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Moyenne'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 25, 3),
(50, 7, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Forte'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 33.3, 2),
(51, 7, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Forte'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 33.3, 3),

(52, 8, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 15, 2),
(53, 8, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 15, 3),
(54, 8, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Nulle à faible'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 0, 2),
(55, 8, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Nulle à faible'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 10, 3),
(56, 8, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Moyenne'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 20, 2),
(57, 8, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Moyenne'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 25, 3),
(58, 8, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Forte'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 33.3, 2),
(59, 8, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Forte'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 33.3, 3),

(60, 9, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 15, 2),
(61, 9, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 15, 3),
(62, 9, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Nulle à faible'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 0, 2),
(63, 9, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Nulle à faible'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 10, 3),
(64, 9, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Moyenne'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 20, 2),
(65, 9, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Moyenne'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 25, 3),
(66, 9, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Forte'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 33.3, 2),
(67, 9, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Forte'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 33.3, 3),

(68, 10, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 10, 1),
(69, 10, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Nulle à faible'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 0, 1),
(70, 10, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Moyenne'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 25, 1),
(71, 10, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Forte'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 50, 1),

(72, 11, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 10, 1),
(73, 11, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Nulle à faible'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 0, 1),
(74, 11, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Moyenne'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 25, 1),
(75, 11, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Forte'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'FONCTIONS_QUALIF')), 50, 1),

(76, 12, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 50, 1),
(77, 12, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Faible (conventionnel / contractuel / inventaire)' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 25, 1),
(78, 12, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Fort (réglementaire / maîtrise foncière)' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 1),

(79, 13, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'OUI' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 1),
(80, 13, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'NON' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 50, 1),

(81, 14, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Non dégradée (bon)' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 1),
(82, 14, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Partiellement dégradée (moyen)' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 25, 1),
(83, 14, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Très fortement dégradée (mauvais)' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 50, 1),
(84, 14, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Non évalué' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 10, 1),

(85, 15, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Non dégradée (bon)' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 1),
(86, 15, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Partiellement dégradée (moyen)' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 25, 1),
(87, 15, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Très fortement dégradée (mauvais)' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 50, 1),
(88, 15, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Non évalué' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 10, 1),

(89, 16, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Zh pas ou peu menacée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'EVAL_GLOB_MENACES')), 0, 1),
(90, 16, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Zh modérément menacée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'EVAL_GLOB_MENACES')), 50, 1),
(91, 16, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Zh fortement menacée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'EVAL_GLOB_MENACES')), 100, 1),
(92, 16, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = 'Non évaluée'  and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'EVAL_GLOB_MENACES')), 25, 1),

(93, 17, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = '07 - zones humides de bas fonds en tête de bassin'), 110, 1),
(94, 17, (SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE label_default = '11 - zones humides ponctuelles'), 20, 1);


INSERT INTO pr_zh.cor_item_value VALUES
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = 'Aucun' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 0, 0),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1 ou 2' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 1, 2),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '2 à 5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 2, 5),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>5' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 6, 999999999),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1 à 4' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 1, 4),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '5 à 7' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 5, 7),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '8 ou 9' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 8, 9),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>9' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 9, 999999999),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '1' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 1, 1),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '2' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 2, 2),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '3' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 3, 3),
((SELECT id_nomenclature FROM ref_nomenclatures.t_nomenclatures WHERE mnemonique = '>3' and id_type = (SELECT id_type FROM ref_nomenclatures.bib_nomenclatures_types WHERE mnemonique = 'HIERARCHY')), 4, 999999999);

COMMIT;
