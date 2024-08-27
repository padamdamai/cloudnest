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

    </>
  );
};

export default Header;
