import React from "react";
import { IoMdPersonAdd } from "react-icons/io";
import { IoLogInSharp } from "react-icons/io5";
import { IoMdCart } from "react-icons/io";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <>
      <div className="md:grid md:grid-cols-4 lg-grid-cols-5 bg-blue-500 ">
        <div className="text-3xl font-bold underline text-center py-2 text-white-900">
          OUR STORE
        </div>
        <div className="md:col-span-2 lg-col-span-3 flex py-2 w-9/12">
          <input
            type="search"
            name=""
            id=""
            className="w-full outline-none px-2 rounded-s-md"
          />
          <button className="bg-orange-300 px-2 rounded-e-md">Search</button>
        </div>
        <div className="flex text-3xl text-orange-300 my-2 justify-evenly">
          <IoMdPersonAdd className="" />
          <IoLogInSharp />
          <a href="/cart">
            <IoMdCart />
          </a>
        </div>
      </div>

      <div className="text-3xl  text-white bg-dark flex justify-evenly">
            <Link to={'/'}>Home</Link>
        <Link to={'/products'}>Products</Link>
        <Link to={'/services'}>services</Link>
        <Link to={'/blogs'}>Blogs</Link>
        <Link to={'/contact'}>Contat</Link>
      </div>

      {/* <nav className="navbar navbar-expand-lg bg-body-tertiary">
  <div className="container-fluid">
    <a className="navbar-brand" href="#">Navbar</a>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <a className="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="#">Link</a>
        </li>
        <li className="nav-item dropdown">
          <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul className="dropdown-menu">
            <li><a className="dropdown-item" href="#">Action</a></li>
            <li><a className="dropdown-item" href="#">Another action</a></li>
            <li><hr className="dropdown-divider"/></li>
            <li><a className="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li className="nav-item">
          <a className="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form className="d-flex" role="search">
        <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button className="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav> */}
    </>
  );
};

export default Header;
