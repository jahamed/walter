select /* p.id as 'professional_id', */ p.gender_id, p.customer_may_contact
, l.id as 'language_id'/* , l.name as 'language' */
, ps.school_id, ps.degree_level_id, ps.degree_area_id
, DATEDIFF(CURDATE(), license.license_date) as 'days_since_licensed`'
, p_spec.specialty_id
, CASE WHEN s.id IS NOT NULL THEN 1 ELSE 0 END as sanctioned 
, CASE WHEN p.claimed_by IS NOT NULL THEN 1 ELSE 0 END as claimed 
from professional p 
join professional_language pl on p.id = pl.professional_id  
join language l on l.id = pl.language_id
join professional_school ps on ps.professional_id = p.id
join license on license.professional_id = p.id
join professional_specialty p_spec on p_spec.professional_id = p.id
left join sanction s on s.license_id = license.id
where license.license_date is not null
ORDER BY RAND() limit 500000;


