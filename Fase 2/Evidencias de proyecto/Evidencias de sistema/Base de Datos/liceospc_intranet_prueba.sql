-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 19-10-2024 a las 22:34:14
-- Versión del servidor: 10.6.19-MariaDB-cll-lve
-- Versión de PHP: 8.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `liceospc_intranet_prueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_curso`
--

CREATE TABLE `app_curso` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `app_curso`
--

INSERT INTO `app_curso` (`id`, `nombre`) VALUES
(1, 'Prekínder A'),
(2, 'Prekínder B'),
(3, 'Kínder A'),
(4, 'Kínder B'),
(5, 'Primero Básico A'),
(6, 'Primero Básico B'),
(7, 'Segundo Básico A'),
(8, 'Segundo Básico B'),
(9, 'Tercero Básico A'),
(10, 'Tercero Básico B'),
(11, 'Cuarto Básico A'),
(12, 'Cuarto Básico B'),
(13, 'Quinto Básico A'),
(14, 'Quinto Básico B'),
(15, 'Sexto Básico A'),
(16, 'Sexto Básico B'),
(17, 'Séptimo Básico A'),
(18, 'Séptimo Básico B'),
(19, 'Octavo Básico A'),
(20, 'Octavo Básico B');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_evento`
--

CREATE TABLE `app_evento` (
  `id` bigint(20) NOT NULL,
  `titulo` varchar(200) NOT NULL,
  `descripcion` longtext DEFAULT NULL,
  `fecha` date NOT NULL,
  `creador_id` int(11) NOT NULL,
  `tipo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `app_evento`
--

INSERT INTO `app_evento` (`id`, `titulo`, `descripcion`, `fecha`, `creador_id`, `tipo`) VALUES
(1, 'Prueba 8to basico a', 'prueba', '2024-10-22', 2, 'otro'),
(9, 'Prueba ', '', '2024-10-29', 2, 'otro'),
(11, 'Prueba 5to básico B', '', '2024-10-19', 2, 'otro'),
(12, 'Prueba ', '', '2024-11-29', 2, 'otro'),
(14, 'Prueba 5to a', '', '2024-10-31', 1, 'otro'),
(15, 'Prueba 5to a', '', '2024-10-19', 2, 'otro'),
(16, 'Prueba 5to Historia', 'Prueba Estadarizada coef 2', '2024-10-23', 2, 'otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_evento_compartido_con`
--

CREATE TABLE `app_evento_compartido_con` (
  `id` bigint(20) NOT NULL,
  `evento_id` bigint(20) NOT NULL,
  `usuarios_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `app_evento_compartido_con`
--

INSERT INTO `app_evento_compartido_con` (`id`, `evento_id`, `usuarios_id`) VALUES
(2, 14, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_horariobase`
--

CREATE TABLE `app_horariobase` (
  `id` bigint(20) NOT NULL,
  `dia_semana` varchar(9) NOT NULL,
  `bloque` varchar(50) NOT NULL,
  `curso_id` bigint(20) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `asignatura` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `app_horariobase`
--

INSERT INTO `app_horariobase` (`id`, `dia_semana`, `bloque`, `curso_id`, `usuario_id`, `asignatura`) VALUES
(1, 'MARTES', '10:20 - 11:50', 9, 1, 'Lenguaje '),
(2, 'LUNES', '10:20 - 11:50', 5, 1, 'Lenguaje'),
(3, 'MARTES', '08:30 - 10:00 Primer bloque', 1, 1, 'Lenguaje'),
(4, 'LUNES', '14:25 - 15:55 Ultimo Bloque', 1, 1, 'Matematica'),
(5, 'LUNES', '08:30 - 10:00 Primer bloque', 14, 1, 'Libre'),
(6, 'LUNES', '10:20 - 11:50 Segundo bloque', 14, 1, 'Matematica'),
(7, 'MARTES', '14:25 - 15:55 Ultimo Bloque', 2, 1, 'Lenguaje '),
(8, 'MIERCOLES', '14:25 - 15:55 Ultimo Bloque', 2, 1, 'Lenguaje'),
(9, 'JUEVES', '08:30 - 10:00 Primer bloque', 3, 1, 'Lenguaje '),
(10, 'VIERNES', '08:30 - 10:00 Primer bloque', 17, 1, 'Lenguaje '),
(11, 'LUNES', '12:10 - 13:40 Tercer bloque', 14, 1, 'libre'),
(12, 'MIERCOLES', '08:30 - 10:00 Primer bloque', 18, 1, 'Matematica'),
(13, 'MIERCOLES', '12:10 - 13:40 Tercer bloque', 15, 1, 'Matematica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_horarioexcepcional`
--

CREATE TABLE `app_horarioexcepcional` (
  `id` bigint(20) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `dia_semana` varchar(9) NOT NULL,
  `bloque` varchar(50) NOT NULL,
  `curso_id` bigint(20) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_usuarios`
--

CREATE TABLE `app_usuarios` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `run` varchar(9) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `rol` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `app_usuarios`
--

INSERT INTO `app_usuarios` (`password`, `last_login`, `is_superuser`, `id_usuario`, `run`, `nombre`, `apellido`, `email`, `is_active`, `is_staff`, `rol`) VALUES
('pbkdf2_sha256$870000$BlgXMn5MxZihf8HPRaCpVv$e8z51OlbhlbP6tT3GjCmYsd1BovmfOxiJJ4BJIQoLlc=', '2024-10-19 13:48:21.033499', 0, 1, '210402713', 'Kevin ', 'albanez', 'ke.albanez@example.com', 1, 0, 'Profesor'),
('pbkdf2_sha256$870000$2AlszYQ9HRs95H9wEbSupK$fei8L4C76fZhXdLKOInG9rpIEDqAvT6BYlGcbC/q03U=', '2024-10-19 13:46:20.997149', 1, 2, '211729899', 'Natasha', 'Gonzalez', NULL, 1, 1, 'Profesor'),
('pbkdf2_sha256$600000$QUtKYLF6DAbPgfw46Js3cC$iqaxnphkl1MMHO2w5sMcAf3awiTrlv5vGGTbUZlhsG4=', NULL, 0, 3, '123456789', 'Juan', 'Ortega', 'juan.ortega@example.com', 1, 0, 'Profesor'),
('pbkdf2_sha256$260000$muQNd6se2qPfM5GJitBIsD$7jwk5VEK2CSF5tfrdYHz6oyH2v8zuZApCEnZ0pJS/DM=', NULL, 0, 4, '999999998', 'josefina', 'lopez', 'jo.lopez@example.com', 1, 0, 'Profesor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_usuarios_groups`
--

CREATE TABLE `app_usuarios_groups` (
  `id` bigint(20) NOT NULL,
  `usuarios_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `app_usuarios_groups`
--

INSERT INTO `app_usuarios_groups` (`id`, `usuarios_id`, `group_id`) VALUES
(1, 1, 2),
(2, 3, 2),
(3, 4, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `app_usuarios_user_permissions`
--

CREATE TABLE `app_usuarios_user_permissions` (
  `id` bigint(20) NOT NULL,
  `usuarios_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(3, 'Asistente'),
(1, 'Directivo'),
(2, 'Profesor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add persona', 6, 'add_persona'),
(22, 'Can change persona', 6, 'change_persona'),
(23, 'Can delete persona', 6, 'delete_persona'),
(24, 'Can view persona', 6, 'view_persona'),
(25, 'Can add horario', 7, 'add_horario'),
(26, 'Can change horario', 7, 'change_horario'),
(27, 'Can delete horario', 7, 'delete_horario'),
(28, 'Can view horario', 7, 'view_horario'),
(29, 'Can add usuarios', 8, 'add_usuarios'),
(30, 'Can change usuarios', 8, 'change_usuarios'),
(31, 'Can delete usuarios', 8, 'delete_usuarios'),
(32, 'Can view usuarios', 8, 'view_usuarios'),
(33, 'Can add curso', 9, 'add_curso'),
(34, 'Can change curso', 9, 'change_curso'),
(35, 'Can delete curso', 9, 'delete_curso'),
(36, 'Can view curso', 9, 'view_curso'),
(37, 'Can add horario base', 10, 'add_horariobase'),
(38, 'Can change horario base', 10, 'change_horariobase'),
(39, 'Can delete horario base', 10, 'delete_horariobase'),
(40, 'Can view horario base', 10, 'view_horariobase'),
(41, 'Can add horario excepcional', 11, 'add_horarioexcepcional'),
(42, 'Can change horario excepcional', 11, 'change_horarioexcepcional'),
(43, 'Can delete horario excepcional', 11, 'delete_horarioexcepcional'),
(44, 'Can view horario excepcional', 11, 'view_horarioexcepcional'),
(45, 'Can add evento', 12, 'add_evento'),
(46, 'Can change evento', 12, 'change_evento'),
(47, 'Can delete evento', 12, 'delete_evento'),
(48, 'Can view evento', 12, 'view_evento');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(9, 'app', 'curso'),
(12, 'app', 'evento'),
(7, 'app', 'horario'),
(10, 'app', 'horariobase'),
(11, 'app', 'horarioexcepcional'),
(6, 'app', 'persona'),
(8, 'app', 'usuarios'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-10-16 20:30:08.428854'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-10-16 20:30:09.691755'),
(3, 'auth', '0001_initial', '2024-10-16 20:30:13.177696'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-10-16 20:30:13.716145'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-10-16 20:30:14.054848'),
(6, 'auth', '0004_alter_user_username_opts', '2024-10-16 20:30:14.403941'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-10-16 20:30:14.747397'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-10-16 20:30:15.085029'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-10-16 20:30:15.427844'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-10-16 20:30:15.771313'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-10-16 20:30:16.118990'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-10-16 20:30:16.655477'),
(13, 'auth', '0011_update_proxy_permissions', '2024-10-16 20:30:17.503937'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-10-16 20:30:17.841840'),
(20, 'sessions', '0001_initial', '2024-10-16 20:30:30.188917'),
(23, 'app', '0001_initial', '2024-10-17 02:02:45.411208'),
(24, 'admin', '0001_initial', '2024-10-17 02:02:47.727628'),
(25, 'admin', '0002_logentry_remove_auto_add', '2024-10-17 02:02:48.078518'),
(26, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-17 02:02:48.425382'),
(27, 'admin', '0004_alter_logentry_user', '2024-10-17 02:02:48.774777'),
(28, 'app', '0002_auto_20241016_1805', '2024-10-17 02:02:49.363372'),
(29, 'app', '0003_auto_20241016_2123', '2024-10-17 02:02:50.734902'),
(30, 'app', '0004_auto_20241016_2302', '2024-10-17 02:02:55.270567'),
(31, 'app', '0005_alter_horariobase_bloque', '2024-10-17 02:29:18.362407'),
(32, 'app', '0006_auto_20241017_0008', '2024-10-17 03:09:08.730856'),
(33, 'app', '0007_evento', '2024-10-18 18:26:50.892095'),
(34, 'app', '0008_evento_tipo', '2024-10-18 19:46:48.059454');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('47wrshr873a04xyjyz47wc4suv05nu3n', '.eJxVjDsOwjAQBe_iGln-rZ1Q0nMGa-1d4wBypDipEHeHSCmgfTPzXiLitta4dV7iROIsjDj9bgnzg9sO6I7tNss8t3WZktwVedAurzPx83K4fwcVe_3WQbGBPBTvHSlnuEAOYJ1nKCkAJgpK0ciaFYXgRmc1QkalodiBLBjx_gDaNzdy:1t29mf:3KzF2r75QGvXNT7z8PjVzHwm-cdYfDSpAke5etOjxWk', '2024-11-02 13:46:21.169279'),
('unaqzgy4smvq5vzl3fu9e5wunwo3ek5x', '.eJxVjDkOwjAUBe_iGln-ON4o6TlD9LeQALKlLBXi7ihSCmjfzLy36XFbx35bdO4nMRdzNqffjZCfWncgD6z3ZrnVdZ7I7oo96GJvTfR1Pdy_gxGXca8piygkJAilBFYfcIiQfXI-xE5cKN67ouS7ADkRkwNQiAMySWY0ny_iSTf4:1t1UQN:-leErXNTidjtCKiBBHaaTp7IqinP7lDeIk0wVcmbaQA', '2024-10-31 17:36:35.925316');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `app_curso`
--
ALTER TABLE `app_curso`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `app_evento`
--
ALTER TABLE `app_evento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_evento_creador_id_29735917_fk_app_usuarios_id_usuario` (`creador_id`);

--
-- Indices de la tabla `app_evento_compartido_con`
--
ALTER TABLE `app_evento_compartido_con`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_evento_compartido_con_evento_id_usuarios_id_db65a6bd_uniq` (`evento_id`,`usuarios_id`),
  ADD KEY `app_evento_compartid_usuarios_id_798a8d78_fk_app_usuar` (`usuarios_id`);

--
-- Indices de la tabla `app_horariobase`
--
ALTER TABLE `app_horariobase`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_horariobase_curso_id_bbf25499_fk_app_curso_id` (`curso_id`),
  ADD KEY `app_horariobase_usuario_id_93ab52a7_fk_app_usuarios_id_usuario` (`usuario_id`);

--
-- Indices de la tabla `app_horarioexcepcional`
--
ALTER TABLE `app_horarioexcepcional`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_horarioexcepcional_curso_id_4d258b5c_fk_app_curso_id` (`curso_id`),
  ADD KEY `app_horarioexcepcion_usuario_id_ff6a32ac_fk_app_usuar` (`usuario_id`);

--
-- Indices de la tabla `app_usuarios`
--
ALTER TABLE `app_usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `run` (`run`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `app_usuarios_groups`
--
ALTER TABLE `app_usuarios_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_usuarios_groups_usuarios_id_group_id_376af848_uniq` (`usuarios_id`,`group_id`),
  ADD KEY `app_usuarios_groups_group_id_4af7852d_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `app_usuarios_user_permissions`
--
ALTER TABLE `app_usuarios_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_usuarios_user_permis_usuarios_id_permission_i_ce87f1db_uniq` (`usuarios_id`,`permission_id`),
  ADD KEY `app_usuarios_user_pe_permission_id_40834834_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_app_usuarios_id_usuario` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `app_curso`
--
ALTER TABLE `app_curso`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `app_evento`
--
ALTER TABLE `app_evento`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `app_evento_compartido_con`
--
ALTER TABLE `app_evento_compartido_con`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `app_horariobase`
--
ALTER TABLE `app_horariobase`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `app_horarioexcepcional`
--
ALTER TABLE `app_horarioexcepcional`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `app_usuarios`
--
ALTER TABLE `app_usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `app_usuarios_groups`
--
ALTER TABLE `app_usuarios_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `app_usuarios_user_permissions`
--
ALTER TABLE `app_usuarios_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `app_evento`
--
ALTER TABLE `app_evento`
  ADD CONSTRAINT `app_evento_creador_id_29735917_fk_app_usuarios_id_usuario` FOREIGN KEY (`creador_id`) REFERENCES `app_usuarios` (`id_usuario`);

--
-- Filtros para la tabla `app_evento_compartido_con`
--
ALTER TABLE `app_evento_compartido_con`
  ADD CONSTRAINT `app_evento_compartid_usuarios_id_798a8d78_fk_app_usuar` FOREIGN KEY (`usuarios_id`) REFERENCES `app_usuarios` (`id_usuario`),
  ADD CONSTRAINT `app_evento_compartido_con_evento_id_cd0f969b_fk_app_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `app_evento` (`id`);

--
-- Filtros para la tabla `app_horariobase`
--
ALTER TABLE `app_horariobase`
  ADD CONSTRAINT `app_horariobase_curso_id_bbf25499_fk_app_curso_id` FOREIGN KEY (`curso_id`) REFERENCES `app_curso` (`id`),
  ADD CONSTRAINT `app_horariobase_usuario_id_93ab52a7_fk_app_usuarios_id_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `app_usuarios` (`id_usuario`);

--
-- Filtros para la tabla `app_horarioexcepcional`
--
ALTER TABLE `app_horarioexcepcional`
  ADD CONSTRAINT `app_horarioexcepcion_usuario_id_ff6a32ac_fk_app_usuar` FOREIGN KEY (`usuario_id`) REFERENCES `app_usuarios` (`id_usuario`),
  ADD CONSTRAINT `app_horarioexcepcional_curso_id_4d258b5c_fk_app_curso_id` FOREIGN KEY (`curso_id`) REFERENCES `app_curso` (`id`);

--
-- Filtros para la tabla `app_usuarios_groups`
--
ALTER TABLE `app_usuarios_groups`
  ADD CONSTRAINT `app_usuarios_groups_group_id_4af7852d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `app_usuarios_groups_usuarios_id_ac538012_fk_app_usuar` FOREIGN KEY (`usuarios_id`) REFERENCES `app_usuarios` (`id_usuario`);

--
-- Filtros para la tabla `app_usuarios_user_permissions`
--
ALTER TABLE `app_usuarios_user_permissions`
  ADD CONSTRAINT `app_usuarios_user_pe_permission_id_40834834_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `app_usuarios_user_pe_usuarios_id_1bd8bff3_fk_app_usuar` FOREIGN KEY (`usuarios_id`) REFERENCES `app_usuarios` (`id_usuario`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_app_usuarios_id_usuario` FOREIGN KEY (`user_id`) REFERENCES `app_usuarios` (`id_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
