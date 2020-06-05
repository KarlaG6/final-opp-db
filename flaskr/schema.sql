DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS career;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS rol;
DROP TABLE IF EXISTS room_type;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS subject_;
DROP TABLE IF EXISTS equipment;

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE career (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_c TEXT NOT NULL,
  faculty TEXT NOT NULL
);

CREATE TABLE rol (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_rl TEXT NOT NULL,
  descript_rl TEXT
);

CREATE TABLE id_type (
  id INTEGER PRIMARY KEY,
  descript_id_t TEXT NOT NULL
);

CREATE TABLE user (
  id INTEGER PRIMARY KEY,
  id_type INTEGER,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  rol_id INTEGER NOT NULL,
  FOREIGN KEY (rol_id) REFERENCES rol (id),
  FOREIGN KEY (id_type) REFERENCES id_type (id)
);

CREATE TABLE room_type (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_r_t TEXT NOT NULL
);

CREATE TABLE room (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_rm TEXT NOT NULL,
  typer INTEGER,
  FOREIGN KEY (typer) REFERENCES room_type (id)
);

CREATE TABLE subject_ (
  id INTEGER PRIMARY KEY,
  name_s TEXT NOT NULL,
  professor_id INTEGER,
  room INTEGER,
  FOREIGN KEY (professor_id) REFERENCES user (id),
  FOREIGN KEY (room) REFERENCES room (id)
);

CREATE TABLE equipment (
  id INTEGER PRIMARY KEY,
  name_e TEXT NOT NULL
);

CREATE TABLE functionary_type (
  id INTEGER PRIMARY KEY,
  name_f_t TEXT NOT NULL
);