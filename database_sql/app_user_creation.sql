-- Insert sample data
INSERT INTO user (email, password, is_admin, name) VALUES ("system", NULL, TRUE, "System"); -- future use
INSERT INTO user (email, password, is_admin, name) VALUES ("root@localhost", "pbkdf2:sha256:260000$fstVNUjfKcKNVoH4$35cf1b3d453e80440b63cd09560d570d87606cbcf0ce3d38504c520d289add1e", TRUE, "Administrator");