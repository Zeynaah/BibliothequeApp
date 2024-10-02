import streamlit as st
import json
import os

# Fichiers pour stocker les données
BOOKS_FILE = "books.json"
USERS_FILE = "users.json"
RESERVES_FILE = "reserves.json"
PRETS_FILE = "prets.json"


# Fonction pour charger les données depuis un fichier JSON
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

# Fonction pour sauvegarder les données dans un fichier JSON
def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)

# Chargement initial des données
if 'books' not in st.session_state:
    st.session_state.books = load_data(BOOKS_FILE)
if 'users' not in st.session_state:
    st.session_state.users = load_data(USERS_FILE)

# Fonction pour ajouter un livre
def add_book(title, author):
    st.session_state.books.append({"title": title, "author": author})
    save_data(st.session_state.books, BOOKS_FILE)

# Fonction pour ajouter un utilisateur
def add_user(name, email):
    st.session_state.users.append({"name": name, "email": email})
    save_data(st.session_state.users, USERS_FILE)




# Fonction pour modifier un livre
def modify_book(index, title, author):
    st.session_state.books[index] = {"title": title, "author": author}
    save_data(st.session_state.books, BOOKS_FILE)

# Fonction pour modifier un utilisateur
def modify_user(index, name, email):
    st.session_state.users[index] = {"name": name, "email": email}
    save_data(st.session_state.users, USERS_FILE)

# Fonction pour supprimer un livre
def delete_book(index):
    del st.session_state.books[index]
    save_data(st.session_state.books, BOOKS_FILE)

# Fonction pour supprimer un utilisateur
def delete_user(index):
    del st.session_state.users[index]
    save_data(st.session_state.users, USERS_FILE)

# Interface Streamlit
st.title("Gestion de Bibliothèque")

# Ajout de livres
st.header("Ajouter un Livre")
book_title = st.text_input("Titre du livre")
book_author = st.text_input("Auteur du livre")
if st.button("Ajouter le Livre"):
    add_book(book_title, book_author)
    st.success("Livre ajouté !")

# Ajout d'utilisateurs
st.header("Ajouter un Utilisateur")
user_name = st.text_input("Nom de l'utilisateur")
user_email = st.text_input("Email de l'utilisateur")
if st.button("Ajouter l'Utilisateur"):
    add_user(user_name, user_email)
    st.success("Utilisateur ajouté !")

# Affichage des livres
st.header("Liste des Livres")
if len(st.session_state.books) > 0:
    for i, book in enumerate(st.session_state.books):
        st.write(f"{i + 1}. {book['title']} par {book['author']}")

    # Sélection pour modifier un livre
    selected_book_index = st.selectbox("Sélectionner un livre à modifier", range(len(st.session_state.books)), format_func=lambda x: st.session_state.books[x]['title'])
    
    # Nouveau titre et auteur pour modification
    new_title = st.text_input("Nouveau Titre", value=st.session_state.books[selected_book_index]['title'])
    new_author = st.text_input("Nouvel Auteur", value=st.session_state.books[selected_book_index]['author'])

    if st.button("Valider Modifications du Livre"):
        modify_book(selected_book_index, new_title, new_author)
        st.success("Livre modifié !")

    if st.button("Supprimer le Livre"):
        delete_book(selected_book_index)
        st.success("Livre supprimé !")

# Affichage des utilisateurs
st.header("Liste des Utilisateurs")
if len(st.session_state.users) > 0:
    for i, user in enumerate(st.session_state.users):
        st.write(f"{i + 1}. {user['name']} - {user['email']}")

    # Sélection pour modifier un utilisateur
    selected_user_index = st.selectbox("Sélectionner un utilisateur à modifier", range(len(st.session_state.users)), format_func=lambda x: st.session_state.users[x]['name'])

    # Nouveau nom et email pour modification
    new_name = st.text_input("Nouveau Nom", value=st.session_state.users[selected_user_index]['name'])
    new_email = st.text_input("Nouvel Email", value=st.session_state.users[selected_user_index]['email'])

    if st.button("Valider Modifications de l'Utilisateur"):
        modify_user(selected_user_index, new_name, new_email)
        st.success("Utilisateur modifié !")

    if st.button("Supprimer l'Utilisateur"):
        delete_user(selected_user_index)
        st.success("Utilisateur supprimé !")


