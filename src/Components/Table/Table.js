import React, { useState, useEffect } from 'react';
import "react-tabulator/lib/styles.css";
import "react-tabulator/css/tabulator_bootstrap5.min.css";
import { ReactTabulator } from 'react-tabulator'
import { fetchData } from './logic';
import { Modal, Button } from 'react-bootstrap';
import ViewModal from "../Modals/ViewModals/ViewModal";

function Table() {
    const [modalOpen, setModalOpen] = useState(false); // Stato per controllare se il modale è aperto o chiuso
    const [selectedRowData, setSelectedRowData] = useState(null); // Stato per memorizzare i dati della riga selezionata
    const [posts, setPosts] = useState([]);

    const rowClickHandler = (e, row) => {
        // Quando viene cliccata una riga, memorizza i dati della riga selezionata e apri il modale
        console.log("Qui entro");
        setSelectedRowData(row.getData());
        setModalOpen(true);
    }

    const closeModal = () => {
        setModalOpen(false);
        setSelectedRowData(null);
    };


    useEffect(() => {
        async function fetchAndSetPosts() {
            try {
                const data = await fetchData();
                setPosts(data);
            } catch (error) {
                console.error('Error setting posts:', error);
            }
        }
        fetchAndSetPosts();

    }, []);

    const columns = [
        { title: "Name", field: "name", width: 150, hozAlign: "left" },
        { title: "Team", field: "team", hozAlign: "left" },
        { title: "GpWin", field: "gpWin", hozAlign: "left" },
        { title: "GpMade", field: "gpMade", hozAlign: "left" },
        { title: "Podiums", field: "podiums", hozAlign: "left" },
        { title: "Points", field: "points", hozAlign: "left" },
        { title: "Fastest Lap", field: "fastLaps", hozAlign: "left" }
    ];


    return (
        <div className="table-container">
            <ReactTabulator
                data={posts}
                columns={columns}
                events={{ rowClick: rowClickHandler }}>
            </ReactTabulator>
            {/* Modale */}
            {modalOpen && <ViewModal  isOpen={modalOpen} closeModal={closeModal} selectedRowData={selectedRowData} />}
        </div>
    );
}



export default Table;
