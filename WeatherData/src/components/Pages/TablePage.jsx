import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Button, message, Space } from 'antd'; 

import TableLog from '../TableLog/TableLog';
import DatePicker_ from '../DatePicker/DatePicker';

function TablePage() {
    const [dataState, setDataState] = useState([]);
    const [loading, setLoading] = useState(false);
    const [startDate, setStartDate] = useState(null); 
    const [endDate, setEndDate] = useState(null); 

    // Function to handle date range change
    const onDateChange = (dates, dateStrings) => {
        setStartDate(dateStrings[0]); 
        setEndDate(dateStrings[1]);   
    };

    // Fetch data when date range is selected
    useEffect(() => {
        if (!startDate || !endDate) return;

        const fetchData = async () => {
            setLoading(true);
            try {
                const apiUrl = `http://localhost:9998/data/?date_start=${startDate}&date_end=${endDate}`;
                const response = await axios.get(apiUrl);
                setDataState(response.data);
            } catch (error) {
                message.error('Failed to load data');
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [startDate, endDate]);

    // Function to handle file download
    const handleDownload = async () => {
        if (!startDate || !endDate) {
            message.warning('Please select a date range before downloading the file.');
            return;
        }

        try {
            const apiUrl = `http://localhost:9998/data/file?date_start=${startDate}&date_end=${endDate}`;
            const response = await axios({
                url: apiUrl,
                method: 'GET',
                responseType: 'blob', // Указание на получение данных в бинарном формате
            });

            // Создаем ссылку для скачивания
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', `data_${startDate}_to_${endDate}.csv`); // Название файла
            document.body.appendChild(link);
            link.click();
            link.remove();
        } catch (error) {
            message.error('Failed to download file');
        }
    };

    return (
        <div>
            <Space direction="vertical" style={{ marginBottom: 20 }}>
                <DatePicker_ onChange={onDateChange} />
                <Button 
                    type="primary" 
                    onClick={handleDownload}
                    disabled={!startDate || !endDate} // Делаем кнопку неактивной, если даты не выбраны
                >
                    Скачать файл
                </Button>
            </Space>
            <TableLog dataState={dataState} loading={loading} />
        </div>
    );
}

export default TablePage;
