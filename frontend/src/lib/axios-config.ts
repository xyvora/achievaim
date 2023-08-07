import axios from 'axios';
import { API } from '$lib/variables';

export const axiosInstance = axios.create({ baseURL: `${API}`, timeout: 5000, params: {} });
