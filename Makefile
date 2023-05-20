start:
	uvicorn track_it.main:app --reload --host 0.0.0.0 --port 8000
test:
	pytest