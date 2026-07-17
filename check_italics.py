import csv

INPUT_CSV = "NB Edits - references_FINAL.csv"
OUTPUT_CSV = "references_still_needing_italics.csv"

ITALIC_PHRASES = [
  "can be",
  "Tech Behind ICE",
  "Drones for Them but Not for Us?",
  "404 Media",
  "Wired",
  "The New York Times",
  "Garbage In, Garbage Out: Face Recognition on Flawed Data",
  "ICE’s EDDIE Program: How ICE Uses Biometric Scanner Tech to Ramp Up Raids",
  "Raiding the Genome: How the United States Government Is Abusing Its Immigration Powers to Amass DNA for Future Policing",
  "Catholic University Journal of Law and Technology",
  "HART Attack: How DHS’s Massive Biometrics Database Will Supercharge Surveillance and Threaten Rights",
  "Homeland Advanced Recognition Technology: DHS Is Building a Massive Database of Personal Information",
  "DHS’s Data Reservoir: ICE and CBP’s Capture and Circulation of Location Information",
  "The Wall Street Journal",
  "Gotta Catch ’Em All: Understanding How IMSI-Catchers Exploit Cell Networks",
  "Cellphones, Law Enforcement, and the Right to Privacy",
  "Leaving the Door Wide Open: Flock Surveillance Systems Expose Washington Data to Immigration Enforcement",
  "Automatic License Plate Readers: Legal Status and Policy Recommendations for Law Enforcement Use",
  "The Intercept",
  "Forbes",
  "The Fight to Protect Our Phones: A Multi-Prong Approach to Spyware Reform",
  "Virtue or Vice? A First Look at Paragon’s Proliferating Spyware Operations",
  "The Logic",
  "Just Security",
  "[DHS] Social Media Monitoring",
  "Lawfare",
  "American Dragnet: Data-Driven Deportation in the 21st Century",
  "Legal Loopholes and Data for Dollars: How Law Enforcement and Intelligence Agencies Are Buying Your Data from Brokers",
  "The Data Broker to Deportation Pipeline: How Thomson Reuters & LexisNexis Share Utility & Commercial Data with ICE",
  "The Guardian",
  "The Washington Post",
  "BYU Law Review",
  "Business Insider",
  "A Realignment for Homeland Security Investigations",
  "The Lever",
  "Financial Times",
  "Automating Deportation: The Artificial Intelligence Behind the Department of Homeland Security’s Immigration Enforcement Regime"
]

# Change these if your CSV uses different header names.
ITALIC_COLUMN = "italic"
LABEL_COLUMN = "label"


def contains_known_italic_phrase(text):
    text_lower = (text or "").lower()

    return any(
        phrase.lower() in text_lower
        for phrase in ITALIC_PHRASES
    )


with open(INPUT_CSV, "r", encoding="utf-8-sig", newline="") as input_file:
    reader = csv.DictReader(input_file)

    if not reader.fieldnames:
        raise ValueError("The input CSV has no headers.")

    if ITALIC_COLUMN not in reader.fieldnames:
        raise ValueError(
            f'Could not find the column "{ITALIC_COLUMN}". '
            f"Available columns: {reader.fieldnames}"
        )

    if LABEL_COLUMN not in reader.fieldnames:
        raise ValueError(
            f'Could not find the column "{LABEL_COLUMN}". '
            f"Available columns: {reader.fieldnames}"
        )

    unmatched_rows = []

    for row in reader:
        italic_value = (row.get(ITALIC_COLUMN) or "").strip().upper()
        label = row.get(LABEL_COLUMN) or ""

        if italic_value == "ITALICS" and not contains_known_italic_phrase(label):
            unmatched_rows.append(row)

    fieldnames = reader.fieldnames


with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(unmatched_rows)


print(f"Found {len(unmatched_rows)} rows still needing italics.")
print(f"Saved to: {OUTPUT_CSV}")