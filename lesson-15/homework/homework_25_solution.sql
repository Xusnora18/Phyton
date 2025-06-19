
-- Step 1: Create the Roster table
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);

-- Step 2: Insert the given data
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);

-- Step 3: Update the name from Jadzia Dax to Ezri Dax
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';

-- Step 4: Select Name and Age where Species is Bajoran
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';
