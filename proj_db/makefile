MAKEFILE_PATH = /home/chinmay/Documents/ASU/fall21/cse412/CSE412-Proj
ROOT = $(MAKEFILE_PATH)/proj_db
DBNAME = vgdb3


setup_postgres:
	@echo "creating folder"
	mkdir $(DBNAME)
	@echo "creating database"
	initdb ./$(DBNAME)
	pg_ctl -D ./$(DBNAME) -o '-k /tmp' start
	createdb $(DBNAME) -p 8888 -h /tmp
	@echo "creating tables"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -f '$(ROOT)/create_tables.sql'
	@echo "importing data"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Videogame FROM '$(ROOT)/Videogames.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Company FROM '$(ROOT)/Company.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Critic FROM '$(ROOT)/Critic.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY AwardPresented FROM '$(ROOT)/AwardPresented.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Given FROM '$(ROOT)/Given.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Backer FROM '$(ROOT)/Backer.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Person FROM '$(ROOT)/Person.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Crew FROM '$(ROOT)/Crew.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Member FROM '$(ROOT)/Member.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Creators FROM '$(ROOT)/Creators.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Rating FROM '$(ROOT)/Rating.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY VideoGameProducer FROM '$(ROOT)/VideoGameProducer.csv' DELIMITER ',' CSV;"
	psql -d $(DBNAME) -p 8888 -h /tmp -q -c "COPY Organization FROM '$(ROOT)/Organization.csv' DELIMITER ',' CSV;"

clean_postgres:
	psql -d $(DBNAME) -p 8888 -h /tmp -q -f drop_tables.sql

nuke:
	pg_ctl -D ./$(DBNAME) stop
	rm -rf $(DBNAME)


.PHONY: setup_postgres

