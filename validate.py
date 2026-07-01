import json
from pathlib import Path
p = Path(__file__).with_name('puzzles.json')
data = json.loads(p.read_text(encoding='utf-8'))
assert isinstance(data, list) and len(data) >= 12
ids = [x['id'] for x in data]
assert len(ids) == len(set(ids)), 'duplicate ids'
required = {'id','title','difficulty','tags','surface','answer','hostNotes','source'}
for item in data:
    missing = required - set(item)
    assert not missing, f"{item.get('id')} missing {missing}"
    assert 1 <= item['difficulty'] <= 5
    assert item['surface'].strip() and item['answer'].strip()
    assert isinstance(item['tags'], list) and item['tags']
    assert isinstance(item['hostNotes'], list) and item['hostNotes']
print(f'OK: {len(data)} puzzles validated')
