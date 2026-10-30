print("===== HEALTH ADVISORY EXPERT SYSTEM =====")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()
cold = input("Do you have cold? (yes/no): ").lower()

if fever == "yes" and cough == "yes":
    print("\nSuggestion: You may have a common respiratory infection.")
    print("Please consult a doctor.")

elif cold == "yes" and cough == "yes":
    print("\nSuggestion: You may have common cold symptoms.")
    print("Take rest and drink enough water.")

elif fever == "yes" and headache == "yes":
    print("\nSuggestion: Fever with headache may need medical attention.")
    print("Please consult a doctor.")

elif cold == "yes":
    print("\nSuggestion: You may have common cold symptoms.")

elif headache == "yes":
    print("\nSuggestion: Take rest and drink enough water.")

else:
    print("\nSuggestion: No matching symptoms found.")

print("\nThank you!")
