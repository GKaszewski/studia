from typing import List
    
def generate_union_part(prefixes: List[str]):
    geom_cte = f'powiat_bytowski_geom'
    union_parts = []
    tables = ['ot_ptwp_a', 'ot_ptzb_a', 'ot_ptlz_a', 'ot_ptrk_a', 'ot_ptut_a', 'ot_pttr_a', 'ot_ptkm_a', 'ot_ptgn_a',
                  'ot_ptpl_a', 'ot_ptso_a', 'ot_ptwz_a', 'ot_ptnz_a']
    for prefix in prefixes:
        for table in tables:
            part = f'''
                SELECT ST_UNION(ST_MakeValid(geometria)) as geometria
                FROM {geom_cte} b, {prefix}.{table} a
                WHERE ST_Intersects(a.geometria, b.geom)
                '''
            union_parts.append(part)
    return union_parts
    

unions = generate_union_part(['powiat_bytowski', 'powiat_koscierski'])

u = f'UNION '.join(unions)
query = f'''
    SELECT ST_UNION(ARRAY({u})) as geometria
'''
with open('queries.txt', 'w') as f:
    f.write(query)
