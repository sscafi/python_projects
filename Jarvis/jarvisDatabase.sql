Table: commands
- id (int, primary key, auto-increment)
- name (varchar(255))
- action (varchar(255))
- created_at (datetime)

Table: inputs
- id (int, primary key, auto-increment)
- command_id (int, foreign key)
- input_text (text)
- created_at (datetime)
