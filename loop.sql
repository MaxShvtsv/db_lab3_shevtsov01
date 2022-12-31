DO $$
    DECLARE
        id phones.phone_id%TYPE;

    BEGIN
        id := 5;
        FOR counter IN 1..5
            LOOP
                INSERT INTO phones(phone_id, label, battery_power,
								   clock_speed, int_memory, m_dep,
								   mobile_wt, camera_focus, blue,
								   dual_sim, four_g)
                VALUES (id + counter, 'Huawei', 2000, 1.9, 128, 0.9, 190, 28, true, true, true);
-- 				   DELETE FROM phones
-- 				   WHERE phones.phone_id = id + counter;
            END LOOP;
    END;
$$;

SELECT *
FROM phones;