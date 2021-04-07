import React from "react";

const Circular = ({ size }) => {
  return (
    <div>
      <div className="loader"></div>
      <style>
        {`
          .loader {
            border: 8px solid #9e9e9e; 
            border-top: 8px solid black; 
            border-radius: 50%;
            width: ${size}px;
            height: ${size}px;
            animation: spin 2s linear infinite;
          }
          
          @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }`}
      </style>
    </div>
  );
};

export default Circular;
