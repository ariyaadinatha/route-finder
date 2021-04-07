import axios from "axios";
import React, { useState } from "react";
import Circular from "../common/Circular";

const Submit = (props) => {
  const { nodeStart, nodeDestination, nodes, adj } = props;
  const [isLoading, setIsLoading] = useState(false);
  const hanldeSubmit = () => {
    if (nodeStart == "" || nodeDestination == "") {
      alert("Please select the node start and destination");
    } else {
      setIsLoading(true);

      const requestBody = {
        nodeStart,
        nodeDestination,
        nodes,
        adj,
      };

      console.log(requestBody);

      axios
        .post("http://localhost:5000/path-a-star", requestBody)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          setIsLoading(false);
        });
    }
  };
  return (
    <>
      <div>
        <h3 className="mb-4 text-center submit-title">Submit</h3>
        <h5 className="mb-4">Node Start : {nodeStart}</h5>
        <h5 className="mb-4">Node Destination : {nodeDestination}</h5>
        <div className="d-flex justify-content-center mb-5">
          <button className="submit-btn" onClick={hanldeSubmit}>
            Find Path
          </button>
        </div>
        {isLoading ? (
          <div className="d-flex justify-content-center">
            <Circular size={45} />
          </div>
        ) : (
          ""
        )}

        <style>
          {`
            .submit-title {
                background: #B98389;
                color: #E4DBD9;
                padding: .5rem 1rem;
                border-radius: 7px; 
            }

            .submit-btn {
                background: #D36582;
                color: white;
                border: none;
                border-radius: 3px;
                padding: .5rem 1.5rem;
                font-size: 1.25rem;
            }

            .submit-btn:focus {
                outline: none;
                border: none;
            }

          `}
        </style>
      </div>
    </>
  );
};

export default Submit;
