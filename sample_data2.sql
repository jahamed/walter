select * from ads;

drop table ads;

drop table p;

CREATE TEMPORARY TABLE ads (INDEX bar (professional_id)) select distinct professional_id from quasi.sponsored_listing_ad union select professional_id from quasi.display_ad;

CREATE temporary table p (INDEX foo (id)) select id , gender_id, customer_may_contact, claimed_by from professional order by RAND() limit 2000000;

select * from p;

select p.id as 'professional_id', p.gender_id, p.customer_may_contact 
, CASE WHEN l.id IS NOT NULL then l.id ELSE 0 END as 'language_id'/* , l.name as 'language' */
, CASE WHEN ps.school_id IS NOT NULL THEN ps.school_id ELSE 0 END as 'school_id'
, CASE WHEN ps.degree_level_id IS NOT NULL THEN ps.degree_level_id ELSE 0 END as 'degree_level'
, CASE WHEN p_spec.specialty_id IS NOT NULL THEN p_spec.specialty_id ELSE 0 END as 'specialty_id'
, CASE WHEN ps.degree_area_id IS NOT NULL THEN ps.degree_area_id ELSE 0 END as 'degree_area'
, CASE WHEN COUNT(DISTINCT p_review.id) = 0 THEN 0 ELSE 1 END as 'has_reviews'
, CASE WHEN s.id IS NOT NULL THEN 1 ELSE 0 END as 'sanctioned' 
, CASE WHEN p.claimed_by IS NOT NULL THEN 1 ELSE 0 END as 'claimed'
, CASE WHEN ads.professional_id is not null
	THEN 1 ELSE 0 END as 'bought_ads'
,	CASE WHEN license.license_date IS NULL then 0 else DATEDIFF(CURDATE(), license.license_date) end as 'days_since_licensed'
from p
left join ads on ads.professional_id = p.id
left join professional_language pl on p.id = pl.professional_id  
left join language l on l.id = pl.language_id
left join professional_school ps on ps.professional_id = p.id
left join license on license.professional_id = p.id
left join professional_specialty p_spec on p_spec.professional_id = p.id
left join professional_review p_review on p_review.professional_id = p.id
left join sanction s on s.license_id = license.id
-- where license.license_date is not null
GROUP BY p.id