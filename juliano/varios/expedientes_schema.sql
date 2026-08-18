BEGIN TRANSACTION;
CREATE TABLE app_undo_cursors (
    scope TEXT PRIMARY KEY,
    entry_id INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE app_undo_entries (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    scope       TEXT NOT NULL,
    action      TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    entity_id   TEXT,
    description TEXT NOT NULL,
    before_state TEXT NOT NULL,
    after_state  TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE aprobacion_jd (
    id_aprobacion_jd      INTEGER PRIMARY KEY AUTOINCREMENT,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    solped                TEXT,
    fecha_presupuesto_base DATE,
    presupuesto_base_bs   REAL,
    tipo_cambio           REAL,
    presupuesto_base_usd  REAL,
    id_plan               INTEGER,
    descripcion_proceso   TEXT,
    cantidad_frentes      INTEGER,
    id_estatus            INTEGER DEFAULT 1,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    tiempo_ejecucion      TEXT,
    observaciones         TEXT,
    notas                 TEXT,
    fecha_creacion        DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion   DATE DEFAULT CURRENT_DATE, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT,
    CONSTRAINT fk_jd_ger FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    CONSTRAINT fk_jd_sup FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    CONSTRAINT fk_jd_em  FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_jd_re  FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_jd_est FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id),
    CONSTRAINT fk_jd_plan FOREIGN KEY (id_plan) REFERENCES cat_plan_contratacion(id)
);
CREATE TABLE aprobacion_jd_documentos (
    id_aprobacion_jd INTEGER NOT NULL REFERENCES aprobacion_jd(id_aprobacion_jd) ON DELETE CASCADE,
    id_documento     INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_aprobacion_jd, id_documento)
);
CREATE TABLE bd_hojas (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    anio           INTEGER NOT NULL UNIQUE,
    activo         INTEGER NOT NULL DEFAULT 0,
    fecha_creacion TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
, nombre TEXT);
INSERT INTO "bd_hojas" VALUES(1,2026,1,'2026-08-17 21:26:11',NULL);
CREATE TABLE cat_art (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE);
INSERT INTO "cat_art" VALUES(1,'5 N - 08');
INSERT INTO "cat_art" VALUES(2,'77 N - 01');
INSERT INTO "cat_art" VALUES(3,'77 N - 02');
INSERT INTO "cat_art" VALUES(4,'77 N - 03');
INSERT INTO "cat_art" VALUES(5,'101 N - 01');
INSERT INTO "cat_art" VALUES(6,'101 N - 02');
INSERT INTO "cat_art" VALUES(7,'101 N - 03');
INSERT INTO "cat_art" VALUES(8,'101 N - 04');
INSERT INTO "cat_art" VALUES(9,'5 N - 06');
CREATE TABLE cat_documento (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    modulo TEXT NOT NULL DEFAULT 'global',
    UNIQUE (nombre, modulo)
);
INSERT INTO "cat_documento" VALUES(1,'ACTA DE INICIO SOLICITUD','expedientes');
INSERT INTO "cat_documento" VALUES(2,'ACTA DE MODIFICACIÓN DEL CONTRATO','expedientes');
INSERT INTO "cat_documento" VALUES(3,'ACTA DE OTRAS CONSIDERACIONES','expedientes');
INSERT INTO "cat_documento" VALUES(4,'ACTA DE OTORGAMIENTO','expedientes');
INSERT INTO "cat_documento" VALUES(5,'NOTIFICACIÓN DE ADJUDICACIÓN','expedientes');
INSERT INTO "cat_documento" VALUES(6,'ACTA DE RESULTADOS DE CALIFICACIÓN Y EVALUACIÓN','expedientes');
INSERT INTO "cat_documento" VALUES(7,'ACTO MOTIVADO','expedientes');
INSERT INTO "cat_documento" VALUES(8,'ANÁLISIS ECONÓMICO','expedientes');
INSERT INTO "cat_documento" VALUES(9,'ACTUALIZACIÓN DE PRESUPUESTO BASE','expedientes');
INSERT INTO "cat_documento" VALUES(10,'ADDENDUM','expedientes');
INSERT INTO "cat_documento" VALUES(12,'CONTRATO','expedientes');
INSERT INTO "cat_documento" VALUES(13,'CONTRATO DE SERVICIOS','expedientes');
INSERT INTO "cat_documento" VALUES(14,'DECISIÓN DE GERENCIA','expedientes');
INSERT INTO "cat_documento" VALUES(15,'DECISIÓN DE GERENCIA INICIO','expedientes');
INSERT INTO "cat_documento" VALUES(16,'DECISIÓN DE GERENCIA MODIFICACIÓN','expedientes');
INSERT INTO "cat_documento" VALUES(18,'ESPECIFICACIONES TÉCNICAS','expedientes');
INSERT INTO "cat_documento" VALUES(19,'JUSTIFICACIÓN','expedientes');
INSERT INTO "cat_documento" VALUES(20,'PRESUPUESTO BASE','expedientes');
INSERT INTO "cat_documento" VALUES(21,'INFORME TÉCNICO DE PRECALIFICACIÓN','expedientes');
CREATE TABLE cat_empresas (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE);
INSERT INTO "cat_empresas" VALUES(1,'PRODUCTORA Y DISTRIBUIDORA VENEZOLANA DE ALIMENTOS, S.A (PDVAL)');
INSERT INTO "cat_empresas" VALUES(2,'TRANSPORTE ROJAS GARCÍA,C.A.');
INSERT INTO "cat_empresas" VALUES(3,'CRANE & HEAVY SERVICE DE VENEZUELA');
INSERT INTO "cat_empresas" VALUES(4,'AGROPECUARIA LA ROSALIERA');
INSERT INTO "cat_empresas" VALUES(5,'SERVICIOS Y SUMINISTROS KAMULY K&M C.A');
INSERT INTO "cat_empresas" VALUES(6,'IMSUPETROL, C.A');
INSERT INTO "cat_empresas" VALUES(7,'CORPORACIÓN SAN REMO, C.A');
INSERT INTO "cat_empresas" VALUES(8,'INVERSIONES ROYPA, S.A');
INSERT INTO "cat_empresas" VALUES(9,'CONCRELAND, C.A');
INSERT INTO "cat_empresas" VALUES(10,'SERVICIOS Y SUMINISTROS DAVNA, C.A.');
INSERT INTO "cat_empresas" VALUES(11,'METALMECANICA CONTRERAS, C.A');
INSERT INTO "cat_empresas" VALUES(12,'SERVICIOS Y TRANSPORTE LOS 2 HERMANOS, C.A');
INSERT INTO "cat_empresas" VALUES(13,'POWERLINE CONSTRUCCIONES, C.A');
CREATE TABLE cat_estatus_detalle (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE, visualizacion TEXT NOT NULL DEFAULT '');
INSERT INTO "cat_estatus_detalle" VALUES(1,'PENDIENTE','pendiente');
INSERT INTO "cat_estatus_detalle" VALUES(2,'FIRMADO','firmado');
INSERT INTO "cat_estatus_detalle" VALUES(3,'DEVUELTO PARA CORRECCIÓN','pendiente');
INSERT INTO "cat_estatus_detalle" VALUES(4,'DEVUELTO SIN FIRMA','pendiente');
INSERT INTO "cat_estatus_detalle" VALUES(5,'SE ENTREGA CON LA FIRMA','firmado');
INSERT INTO "cat_estatus_detalle" VALUES(7,'SE RECIBE PARA LA FIRMA','pendiente');
CREATE TABLE cat_gerencia (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE);
INSERT INTO "cat_gerencia" VALUES(1,'SIHO-A');
INSERT INTO "cat_gerencia" VALUES(2,'TÉCNICA');
INSERT INTO "cat_gerencia" VALUES(3,'OPERACIONES');
INSERT INTO "cat_gerencia" VALUES(4,'SSGG');
INSERT INTO "cat_gerencia" VALUES(5,'JURÍDICO');
INSERT INTO "cat_gerencia" VALUES(6,'FINANZAS');
INSERT INTO "cat_gerencia" VALUES(7,'CONTRATACIÓN');
INSERT INTO "cat_gerencia" VALUES(8,'RRHH');
INSERT INTO "cat_gerencia" VALUES(9,'ASUNTOS GUBERNAMENTALES');
INSERT INTO "cat_gerencia" VALUES(10,'COMISIÓN');
INSERT INTO "cat_gerencia" VALUES(11,'PROCURA');
INSERT INTO "cat_gerencia" VALUES(12,'CONTROL DE DOCUMENTOS');
INSERT INTO "cat_gerencia" VALUES(13,'ASUNTOS PÚBLICOS');
CREATE TABLE cat_hojas (
    tabla    TEXT NOT NULL,
    id_valor INTEGER NOT NULL,
    id_hoja  INTEGER NOT NULL REFERENCES bd_hojas(id) ON DELETE CASCADE,
    PRIMARY KEY (tabla, id_valor, id_hoja)
) WITHOUT ROWID;
INSERT INTO "cat_hojas" VALUES('cat_art',1,1);
INSERT INTO "cat_hojas" VALUES('cat_art',2,1);
INSERT INTO "cat_hojas" VALUES('cat_art',3,1);
INSERT INTO "cat_hojas" VALUES('cat_art',4,1);
INSERT INTO "cat_hojas" VALUES('cat_art',5,1);
INSERT INTO "cat_hojas" VALUES('cat_art',6,1);
INSERT INTO "cat_hojas" VALUES('cat_art',7,1);
INSERT INTO "cat_hojas" VALUES('cat_art',8,1);
INSERT INTO "cat_hojas" VALUES('cat_art',9,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',1,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',2,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',3,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',4,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',5,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',6,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',7,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',8,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',9,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',10,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',12,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',13,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',14,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',15,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',16,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',18,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',19,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',20,1);
INSERT INTO "cat_hojas" VALUES('cat_documento',21,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',1,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',2,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',3,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',4,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',5,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',6,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',7,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',8,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',9,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',10,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',11,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',12,1);
INSERT INTO "cat_hojas" VALUES('cat_empresas',13,1);
INSERT INTO "cat_hojas" VALUES('cat_estatus_detalle',1,1);
INSERT INTO "cat_hojas" VALUES('cat_estatus_detalle',2,1);
INSERT INTO "cat_hojas" VALUES('cat_estatus_detalle',3,1);
INSERT INTO "cat_hojas" VALUES('cat_estatus_detalle',4,1);
INSERT INTO "cat_hojas" VALUES('cat_estatus_detalle',5,1);
INSERT INTO "cat_hojas" VALUES('cat_estatus_detalle',7,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',1,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',2,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',3,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',4,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',5,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',6,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',7,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',8,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',9,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',10,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',11,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',12,1);
INSERT INTO "cat_hojas" VALUES('cat_gerencia',13,1);
INSERT INTO "cat_hojas" VALUES('cat_modalidad',1,1);
INSERT INTO "cat_hojas" VALUES('cat_modalidad',2,1);
INSERT INTO "cat_hojas" VALUES('cat_modalidad',3,1);
INSERT INTO "cat_hojas" VALUES('cat_modalidad',4,1);
INSERT INTO "cat_hojas" VALUES('cat_plan_contratacion',1,1);
INSERT INTO "cat_hojas" VALUES('cat_plan_contratacion',2,1);
INSERT INTO "cat_hojas" VALUES('cat_plan_contratacion',3,1);
INSERT INTO "cat_hojas" VALUES('cat_plan_contratacion',4,1);
INSERT INTO "cat_hojas" VALUES('cat_resultado_proceso',1,1);
INSERT INTO "cat_hojas" VALUES('cat_resultado_proceso',2,1);
INSERT INTO "cat_hojas" VALUES('cat_resultado_proceso',3,1);
INSERT INTO "cat_hojas" VALUES('cat_resultado_proceso',4,1);
INSERT INTO "cat_hojas" VALUES('cat_resultado_proceso',5,1);
INSERT INTO "cat_hojas" VALUES('cat_resultado_proceso',6,1);
INSERT INTO "cat_hojas" VALUES('cat_resultado_proceso',7,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',1,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',2,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',3,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',4,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',5,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',6,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',7,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',8,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',9,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',10,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',11,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',12,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',13,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',14,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',15,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',16,1);
INSERT INTO "cat_hojas" VALUES('cat_superintendencia',17,1);
INSERT INTO "cat_hojas" VALUES('cat_tipo_contrato',1,1);
INSERT INTO "cat_hojas" VALUES('cat_tipo_contrato',2,1);
INSERT INTO "cat_hojas" VALUES('cat_tipo_contrato',3,1);
CREATE TABLE cat_modalidad (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE);
INSERT INTO "cat_modalidad" VALUES(1,'CONCURSO ABIERTO');
INSERT INTO "cat_modalidad" VALUES(2,'CONCURSO CERRADO');
INSERT INTO "cat_modalidad" VALUES(3,'CONSULTA DE PRECIOS');
INSERT INTO "cat_modalidad" VALUES(4,'CONTRATACIÓN DIRECTA');
CREATE TABLE cat_plan_contratacion (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE);
INSERT INTO "cat_plan_contratacion" VALUES(1,'ARRASTRE 2025');
INSERT INTO "cat_plan_contratacion" VALUES(2,'PLAN 2026');
INSERT INTO "cat_plan_contratacion" VALUES(3,'ADICIONAL (DIRECTOS) 2026');
INSERT INTO "cat_plan_contratacion" VALUES(4,'PLAN-ADICIONAL 2026');
CREATE TABLE cat_responsables (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE);
CREATE TABLE cat_resultado_proceso (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE);
INSERT INTO "cat_resultado_proceso" VALUES(1,'ADJUDICADO');
INSERT INTO "cat_resultado_proceso" VALUES(2,'DESIERTO 113 # 1');
INSERT INTO "cat_resultado_proceso" VALUES(3,'DESIERTO 113 # 2');
INSERT INTO "cat_resultado_proceso" VALUES(4,'DESIERTO 113 # 3');
INSERT INTO "cat_resultado_proceso" VALUES(5,'DESIERTO 113 # 4');
INSERT INTO "cat_resultado_proceso" VALUES(6,'DESIERTO 113 # 5');
INSERT INTO "cat_resultado_proceso" VALUES(7,'DAR POR TERMINADO');
CREATE TABLE cat_superintendencia (
    id INTEGER PRIMARY KEY,
    nombre TEXT UNIQUE,
    id_gerencia INTEGER,
    CONSTRAINT fk_sup_ger FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id)
);
INSERT INTO "cat_superintendencia" VALUES(1,'SIHO-A',1);
INSERT INTO "cat_superintendencia" VALUES(2,'INFRAESTRUCTURA',2);
INSERT INTO "cat_superintendencia" VALUES(3,'PERFORACIÓN',2);
INSERT INTO "cat_superintendencia" VALUES(4,'YACIMIENTOS',2);
INSERT INTO "cat_superintendencia" VALUES(5,'OPTIMIZACIÓN',2);
INSERT INTO "cat_superintendencia" VALUES(6,'OPERACIÓN DE PRODUCCIÓN',3);
INSERT INTO "cat_superintendencia" VALUES(7,'MANTENIMIENTO',3);
INSERT INTO "cat_superintendencia" VALUES(8,'SSGG',4);
INSERT INTO "cat_superintendencia" VALUES(9,'JURÍDICO',5);
INSERT INTO "cat_superintendencia" VALUES(10,'FINANZAS',6);
INSERT INTO "cat_superintendencia" VALUES(11,'CONTRATACIÓN',7);
INSERT INTO "cat_superintendencia" VALUES(12,'RRHH',8);
INSERT INTO "cat_superintendencia" VALUES(13,'ASUNTOS GUBERNAMENTALES',9);
INSERT INTO "cat_superintendencia" VALUES(14,'COMISIÓN',10);
INSERT INTO "cat_superintendencia" VALUES(15,'PROCURA',11);
INSERT INTO "cat_superintendencia" VALUES(16,'CONTROL DE DOCUMENTOS',12);
INSERT INTO "cat_superintendencia" VALUES(17,'ASUNTOS PÚBLICOS',13);
CREATE TABLE cat_tipo_contrato (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE);
INSERT INTO "cat_tipo_contrato" VALUES(1,'PU');
INSERT INTO "cat_tipo_contrato" VALUES(2,'SG');
INSERT INTO "cat_tipo_contrato" VALUES(3,'MIXTO');
CREATE TABLE certificacion_bdu (
    id_certificacion_bdu  INTEGER PRIMARY KEY AUTOINCREMENT,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    presupuesto_base_total_usd REAL,
    monto_adjudicado_total_usd REAL,
    monto_contrato        REAL,
    monto_ejecutado       REAL,
    monto_pagado          REAL,
    id_estatus            INTEGER DEFAULT 1,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    observaciones         TEXT,
    notas                 TEXT,
    fecha_creacion        DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion   DATE DEFAULT CURRENT_DATE, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT,
    CONSTRAINT fk_bdu_ger FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    CONSTRAINT fk_bdu_sup FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    CONSTRAINT fk_bdu_em  FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_bdu_re  FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_bdu_est FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE certificacion_bdu_documentos (
    id_certificacion_bdu INTEGER NOT NULL REFERENCES certificacion_bdu(id_certificacion_bdu) ON DELETE CASCADE,
    id_documento         INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_certificacion_bdu, id_documento)
);
CREATE TABLE expediente_documentos (
    id_expediente INTEGER NOT NULL REFERENCES expedientes(id_expediente) ON DELETE CASCADE,
    id_documento  INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_expediente, id_documento)
);
CREATE TABLE expediente_frentes_adicionales (
    id_frente               INTEGER PRIMARY KEY AUTOINCREMENT,
    id_expediente           INTEGER NOT NULL REFERENCES expedientes(id_expediente) ON DELETE CASCADE,
    orden                   INTEGER NOT NULL CHECK (orden >= 2),
    id_empresa              INTEGER REFERENCES cat_empresas(id) ON DELETE RESTRICT,
    monto_adjudicado_bs     REAL CHECK (monto_adjudicado_bs IS NULL OR monto_adjudicado_bs >= 0),
    monto_adjudicado_usd    REAL CHECK (monto_adjudicado_usd IS NULL OR monto_adjudicado_usd >= 0),
    UNIQUE (id_expediente, orden)
);
CREATE TABLE expedientes (
    id_expediente           INTEGER PRIMARY KEY AUTOINCREMENT,
    solped                  TEXT,
    id_gerencia             INTEGER,
    id_superintendencia     INTEGER,
    id_emisor               INTEGER,
    fecha_presupuesto_base  DATE,
    presupuesto_base_usd    REAL,
    tipo_cambio             REAL,
    presupuesto_base_bs     REAL,
    id_plan                 INTEGER,
    descripcion_proceso     TEXT,
    id_modalidad            INTEGER,
    id_art                  INTEGER,
    id_tipo_contrato        INTEGER,
    nro_acta_apertura       TEXT,
    cantidad_frentes        INTEGER,
    nro_resolucion_jd       TEXT,
    id_estatus              INTEGER DEFAULT 1,
    fecha_recibido          DATE,
    fecha_devuelto          DATE,
    id_receptor             INTEGER,
    nro_proceso             TEXT,
    id_resultado            INTEGER,
    nro_contrato_sicac      TEXT,
    nro_contrato_sap        TEXT,
    id_empresa              INTEGER,
    tiempo_ejecucion        TEXT,
    monto_adjudicado_bs     REAL,
    monto_adjudicado_usd    REAL,
    fecha_firma_contrato    DATE,
    observaciones           TEXT,
    notas                   TEXT,
    fecha_creacion          DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion     DATE DEFAULT CURRENT_DATE, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT,
    CONSTRAINT fk_exp_ger      FOREIGN KEY (id_gerencia)         REFERENCES cat_gerencia(id),
    CONSTRAINT fk_exp_sup      FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    CONSTRAINT fk_exp_emisor   FOREIGN KEY (id_emisor)           REFERENCES cat_responsables(id),
    CONSTRAINT fk_exp_receptor FOREIGN KEY (id_receptor)         REFERENCES cat_responsables(id),
    CONSTRAINT fk_exp_plan     FOREIGN KEY (id_plan)             REFERENCES cat_plan_contratacion(id),
    CONSTRAINT fk_exp_mod      FOREIGN KEY (id_modalidad)        REFERENCES cat_modalidad(id),
    CONSTRAINT fk_exp_art      FOREIGN KEY (id_art)              REFERENCES cat_art(id),
    CONSTRAINT fk_exp_tc       FOREIGN KEY (id_tipo_contrato)    REFERENCES cat_tipo_contrato(id),
    CONSTRAINT fk_exp_est      FOREIGN KEY (id_estatus)          REFERENCES cat_estatus_detalle(id),
    CONSTRAINT fk_exp_res      FOREIGN KEY (id_resultado)        REFERENCES cat_resultado_proceso(id),
    CONSTRAINT fk_exp_emp      FOREIGN KEY (id_empresa)          REFERENCES cat_empresas(id)
);
CREATE TABLE hist_aprobacion_jd (
    id_movimiento         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aprobacion_jd      INTEGER NOT NULL,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    solped                TEXT,
    fecha_presupuesto_base DATE,
    presupuesto_base_bs   REAL,
    tipo_cambio           REAL,
    presupuesto_base_usd  REAL,
    id_plan               INTEGER,
    descripcion_proceso   TEXT,
    cantidad_frentes      INTEGER,
    id_estatus            INTEGER,
    documentos            TEXT,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    tiempo_ejecucion      TEXT,
    observaciones         TEXT,
    notas                 TEXT,
    FOREIGN KEY (id_aprobacion_jd) REFERENCES aprobacion_jd(id_aprobacion_jd),
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id),
    FOREIGN KEY (id_plan) REFERENCES cat_plan_contratacion(id)
);
CREATE TABLE hist_certificacion_bdu (
    id_movimiento         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_certificacion_bdu  INTEGER NOT NULL,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    presupuesto_base_total_usd REAL,
    monto_adjudicado_total_usd REAL,
    monto_contrato        REAL,
    monto_ejecutado       REAL,
    monto_pagado          REAL,
    id_estatus            INTEGER,
    documentos            TEXT,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    observaciones         TEXT,
    notas                 TEXT,
    FOREIGN KEY (id_certificacion_bdu) REFERENCES certificacion_bdu(id_certificacion_bdu),
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE hist_memorandums (
    id_movimiento         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_memorandum         INTEGER NOT NULL,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    asunto                TEXT,
    id_estatus            INTEGER,
    documentos            TEXT,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    observaciones         TEXT,
    notas                 TEXT,
    FOREIGN KEY (id_memorandum) REFERENCES memorandums(id_memorandum),
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE hist_recobros (
    id_movimiento INTEGER PRIMARY KEY AUTOINCREMENT,
    id_recobro INTEGER NOT NULL,
    id_gerencia INTEGER,
    id_superintendencia INTEGER,
    id_emisor INTEGER,
    asunto TEXT,
    fecha_inicio DATE,
    fecha_final DATE,
    servicios REAL,
    beneficios REAL,
    nota_debito_reverso REAL,
    costo_servicio_usd REAL,
    id_estatus INTEGER,
    documentos TEXT,
    fecha_recibido DATE,
    fecha_devuelto DATE,
    id_receptor INTEGER,
    observaciones TEXT,
    notas TEXT, fechas_adicionales TEXT,
    FOREIGN KEY (id_recobro) REFERENCES recobros(id_recobro),
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE hist_reposos_medicos (
    id_movimiento         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_reposo_medico      INTEGER NOT NULL,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    dias_periodo          INTEGER,
    fecha_desde           DATE,
    fecha_hasta           DATE,
    id_estatus            INTEGER,
    documentos            TEXT,
    fecha_recibido        DATE,
    observaciones         TEXT,
    notas                 TEXT,
    FOREIGN KEY (id_reposo_medico) REFERENCES reposos_medicos(id_reposo_medico),
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE hist_req_materiales (
    id_movimiento         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_requisicion        INTEGER NOT NULL,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    descripcion_materiales TEXT,
    serial_equipo         TEXT,
    pase_sicesma          TEXT,
    id_estatus            INTEGER,
    documentos            TEXT,
    observaciones_entrega TEXT,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    observaciones         TEXT,
    notas                 TEXT,
    FOREIGN KEY (id_requisicion) REFERENCES req_materiales(id_requisicion),
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE hist_vacaciones (
    id_movimiento         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_vacacion           INTEGER NOT NULL,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    anio                  INTEGER,
    cantidad_dias         INTEGER,
    fecha_desde           DATE,
    fecha_hasta           DATE,
    id_estatus            INTEGER,
    documentos            TEXT,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    observaciones         TEXT,
    notas                 TEXT,
    FOREIGN KEY (id_vacacion) REFERENCES vacaciones(id_vacacion),
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE hist_valuaciones (
    id_movimiento         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_valuacion          INTEGER NOT NULL,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    solped                TEXT,
    presupuesto_base_bs   REAL,
    presupuesto_base_usd  REAL,
    descripcion_proceso   TEXT,
    id_estatus            INTEGER,
    documentos            TEXT,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    nro_proceso           TEXT,
    nro_contrato_sicac    TEXT,
    nro_contrato_sap      TEXT,
    id_empresa            INTEGER,
    tiempo_ejecucion      TEXT,
    monto_adjudicado_bs   REAL,
    monto_adjudicado_usd  REAL,
    periodo_valuacion_desde DATE,
    periodo_valuacion_hasta DATE,
    monto_valuacion       REAL,
    nro_proforma          TEXT,
    observaciones         TEXT,
    notas                 TEXT, tipo_cambio REAL,
    FOREIGN KEY (id_valuacion) REFERENCES valuaciones(id_valuacion),
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id),
    FOREIGN KEY (id_empresa) REFERENCES cat_empresas(id)
);
CREATE TABLE historial_movimientos (
    id_movimiento           INTEGER PRIMARY KEY AUTOINCREMENT,
    id_expediente           INTEGER NOT NULL,
    solped                  TEXT,
    id_gerencia             INTEGER,
    id_superintendencia     INTEGER,
    id_emisor               INTEGER,
    id_receptor             INTEGER,
    id_plan                 INTEGER,
    id_modalidad            INTEGER,
    id_art                  INTEGER,
    id_tipo_contrato        INTEGER,
    id_estatus              INTEGER,
    id_resultado            INTEGER,
    id_empresa              INTEGER,
    documentos              TEXT,
    fecha_recibido          DATE,
    fecha_devuelto          DATE,
    fecha_presupuesto_base  DATE,
    fecha_firma_contrato    DATE,
    nro_proceso             TEXT,
    nro_acta_apertura       TEXT,
    nro_resolucion_jd       TEXT,
    nro_contrato_sicac      TEXT,
    nro_contrato_sap        TEXT,
    descripcion_proceso     TEXT,
    presupuesto_base_usd    REAL,
    presupuesto_base_bs     REAL,
    tipo_cambio             REAL,
    monto_adjudicado_usd    REAL,
    monto_adjudicado_bs     REAL,
    tiempo_ejecucion        TEXT,
    cantidad_frentes        INTEGER,
    observaciones           TEXT,
    notas                   TEXT,
    fecha_creacion          DATE DEFAULT CURRENT_DATE, frentes_adicionales TEXT NOT NULL DEFAULT '[]',
    FOREIGN KEY (id_expediente)       REFERENCES expedientes(id_expediente),
    FOREIGN KEY (id_gerencia)         REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor)           REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor)         REFERENCES cat_responsables(id),
    FOREIGN KEY (id_plan)             REFERENCES cat_plan_contratacion(id),
    FOREIGN KEY (id_modalidad)        REFERENCES cat_modalidad(id),
    FOREIGN KEY (id_art)              REFERENCES cat_art(id),
    FOREIGN KEY (id_tipo_contrato)    REFERENCES cat_tipo_contrato(id),
    FOREIGN KEY (id_estatus)          REFERENCES cat_estatus_detalle(id),
    FOREIGN KEY (id_resultado)        REFERENCES cat_resultado_proceso(id),
    FOREIGN KEY (id_empresa)          REFERENCES cat_empresas(id)
);
CREATE TABLE memorandums (
    id_memorandum         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    asunto                TEXT,
    id_estatus            INTEGER DEFAULT 1,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    observaciones         TEXT,
    notas                 TEXT,
    fecha_creacion        DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion   DATE DEFAULT CURRENT_DATE, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT,
    CONSTRAINT fk_mem_ger FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    CONSTRAINT fk_mem_sup FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    CONSTRAINT fk_mem_em  FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_mem_re  FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_mem_est FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE memorandums_documentos (
    id_memorandum INTEGER NOT NULL REFERENCES memorandums(id_memorandum) ON DELETE CASCADE,
    id_documento  INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_memorandum, id_documento)
);
CREATE TABLE papelera (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modulo TEXT NOT NULL,
    id_registro INTEGER NOT NULL,
    datos_json TEXT NOT NULL,
    fecha_eliminacion TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
, id_hoja INTEGER NOT NULL DEFAULT 1);
CREATE TABLE recobros (
    id_recobro INTEGER PRIMARY KEY AUTOINCREMENT,
    id_gerencia INTEGER,
    id_superintendencia INTEGER,
    id_emisor INTEGER,
    asunto TEXT,
    fecha_inicio DATE,
    fecha_final DATE,
    servicios REAL,
    beneficios REAL,
    nota_debito_reverso REAL,
    costo_servicio_usd REAL,
    id_estatus INTEGER DEFAULT 1,
    fecha_recibido DATE,
    fecha_devuelto DATE,
    id_receptor INTEGER,
    observaciones TEXT,
    notas TEXT,
    fecha_creacion DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion DATE DEFAULT CURRENT_DATE, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT, fechas_adicionales TEXT,
    FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE recobros_documentos (
    id_recobro INTEGER NOT NULL REFERENCES recobros(id_recobro) ON DELETE CASCADE,
    id_documento INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_recobro, id_documento)
);
CREATE TABLE reposos_medicos (
    id_reposo_medico      INTEGER PRIMARY KEY AUTOINCREMENT,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    dias_periodo          INTEGER,
    fecha_desde           DATE,
    fecha_hasta           DATE,
    id_estatus            INTEGER DEFAULT 1,
    fecha_recibido        DATE,
    observaciones         TEXT,
    notas                 TEXT,
    fecha_creacion        DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion   DATE DEFAULT CURRENT_DATE, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT,
    CONSTRAINT fk_rep_ger FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    CONSTRAINT fk_rep_sup FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    CONSTRAINT fk_rep_em  FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_rep_est FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE reposos_medicos_documentos (
    id_reposo_medico INTEGER NOT NULL REFERENCES reposos_medicos(id_reposo_medico) ON DELETE CASCADE,
    id_documento     INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_reposo_medico, id_documento)
);
CREATE TABLE req_materiales (
    id_requisicion        INTEGER PRIMARY KEY AUTOINCREMENT,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    descripcion_materiales TEXT,
    serial_equipo         TEXT,
    pase_sicesma          TEXT,
    id_estatus            INTEGER DEFAULT 1,
    observaciones_entrega TEXT,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    observaciones         TEXT,
    notas                 TEXT,
    fecha_creacion        DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion   DATE DEFAULT CURRENT_DATE, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT,
    CONSTRAINT fk_req_ger FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    CONSTRAINT fk_req_sup FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    CONSTRAINT fk_req_em  FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_req_re  FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_req_est FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE req_materiales_documentos (
    id_requisicion INTEGER NOT NULL REFERENCES req_materiales(id_requisicion) ON DELETE CASCADE,
    id_documento   INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_requisicion, id_documento)
);
CREATE TABLE ruta_procesos_cronograma (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    id_junta_proceso INTEGER NOT NULL REFERENCES ruta_procesos_junta_proceso(id) ON DELETE CASCADE,
    fecha            TEXT    NOT NULL,
    id_leyenda       INTEGER NOT NULL REFERENCES ruta_procesos_leyenda(id) ON DELETE RESTRICT,
    nota             TEXT    DEFAULT ''
);
CREATE TABLE ruta_procesos_historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    action TEXT NOT NULL,
    before_state TEXT NOT NULL,
    after_state TEXT NOT NULL
);
CREATE TABLE ruta_procesos_historico_cursor (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    pos INTEGER NOT NULL DEFAULT 0
);
INSERT INTO "ruta_procesos_historico_cursor" VALUES(1,0);
CREATE TABLE ruta_procesos_hoja (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT    NOT NULL
);
CREATE TABLE ruta_procesos_junta (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    id_hoja     INTEGER NOT NULL REFERENCES ruta_procesos_hoja(id) ON DELETE CASCADE,
    numero      TEXT    NOT NULL,
    consecutiva INTEGER NOT NULL,
    fecha       TEXT    NOT NULL,
    nombre      TEXT    NOT NULL DEFAULT 'JUNTA DIRECTIVA',
    UNIQUE(id_hoja, numero)
);
CREATE TABLE ruta_procesos_junta_leyenda (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_junta   INTEGER NOT NULL REFERENCES ruta_procesos_junta(id) ON DELETE CASCADE,
    id_leyenda INTEGER NOT NULL REFERENCES ruta_procesos_leyenda(id) ON DELETE CASCADE,
    orden      INTEGER NOT NULL DEFAULT 0,
    UNIQUE(id_junta, id_leyenda)
);
CREATE TABLE ruta_procesos_junta_proceso (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    id_junta  INTEGER NOT NULL REFERENCES ruta_procesos_junta(id) ON DELETE CASCADE,
    numero    INTEGER NOT NULL,
    proceso   TEXT    NOT NULL,
    UNIQUE(id_junta, numero)
);
CREATE TABLE ruta_procesos_junta_semana (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    id_junta     INTEGER NOT NULL REFERENCES ruta_procesos_junta(id) ON DELETE CASCADE,
    numero       INTEGER NOT NULL,
    fecha_inicio TEXT    NOT NULL,
    fecha_fin    TEXT    NOT NULL,
    UNIQUE(id_junta, numero)
);
CREATE TABLE ruta_procesos_leyenda (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre    TEXT    NOT NULL,
    color     TEXT    NOT NULL DEFAULT '#FFFFFF',
    ambito    TEXT    NOT NULL DEFAULT 'junta',
    id_hoja   INTEGER REFERENCES ruta_procesos_hoja(id) ON DELETE CASCADE,
    bloqueado INTEGER DEFAULT 0
);
INSERT INTO "ruta_procesos_leyenda" VALUES(1,'ACTIVIDADES PREVIAS (UNIDAD USUARIA)','#22C55E','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(2,'INICIO (CONTRATACIÓN)','#2563EB','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(3,'VENTA DE PLIEGO DE CONDICIONES (CONTRATACIÓN)','#C08552','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(4,'INICIO (COMISIÓN)','#EAB308','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(5,'APERTURA DE OFERTAS','#EF4444','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(6,'ANÁLISIS TÉCNICO','#F97316','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(7,'ANÁLISIS ECONÓMICO','#7C3AED','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(8,'RESULTADOS (COMISIÓN)','#A855F7','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(9,'APROBACIÓN PRESIDENCIA','#111827','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(10,'CONTROL DE DOCUMENTOS PRESIDENCIA','#38BDF8','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(11,'INSPECCIÓN TECNICA SIAHO','#4ADE80','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(12,'RESULTADOS (CONTRATACIÓN)','#D946EF','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(13,'EN ESPERA DE DOCUMENTOS PARA FIRMA DEL CONTRATO (CONTRATACIÓN)','#94A3B8','global',NULL,0);
INSERT INTO "ruta_procesos_leyenda" VALUES(14,'EN ELABORACION DE CONTRATO','#EC4899','global',NULL,0);
CREATE TABLE vacaciones (
    id_vacacion           INTEGER PRIMARY KEY AUTOINCREMENT,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    anio                  INTEGER,
    cantidad_dias         INTEGER,
    fecha_desde           DATE,
    fecha_hasta           DATE,
    id_estatus            INTEGER DEFAULT 1,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    observaciones         TEXT,
    notas                 TEXT,
    fecha_creacion        DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion   DATE DEFAULT CURRENT_DATE, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT,
    CONSTRAINT fk_vac_ger FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    CONSTRAINT fk_vac_sup FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    CONSTRAINT fk_vac_em  FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_vac_re  FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_vac_est FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id)
);
CREATE TABLE vacaciones_documentos (
    id_vacacion  INTEGER NOT NULL REFERENCES vacaciones(id_vacacion) ON DELETE CASCADE,
    id_documento INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_vacacion, id_documento)
);
CREATE TABLE valuaciones (
    id_valuacion          INTEGER PRIMARY KEY AUTOINCREMENT,
    id_gerencia           INTEGER,
    id_superintendencia   INTEGER,
    id_emisor             INTEGER,
    solped                TEXT,
    presupuesto_base_bs   REAL,
    presupuesto_base_usd  REAL,
    descripcion_proceso   TEXT,
    id_estatus            INTEGER DEFAULT 1,
    fecha_recibido        DATE,
    fecha_devuelto        DATE,
    id_receptor           INTEGER,
    nro_proceso           TEXT,
    nro_contrato_sicac    TEXT,
    nro_contrato_sap      TEXT,
    id_empresa            INTEGER,
    tiempo_ejecucion      TEXT,
    monto_adjudicado_bs   REAL,
    monto_adjudicado_usd  REAL,
    periodo_valuacion_desde DATE,
    periodo_valuacion_hasta DATE,
    monto_valuacion       REAL,
    nro_proforma          TEXT,
    observaciones         TEXT,
    notas                 TEXT,
    fecha_creacion        DATE DEFAULT CURRENT_DATE,
    fecha_actualizacion   DATE DEFAULT CURRENT_DATE, tipo_cambio REAL, id_hoja INTEGER NOT NULL DEFAULT 1, documentos_texto TEXT,
    CONSTRAINT fk_val_ger FOREIGN KEY (id_gerencia) REFERENCES cat_gerencia(id),
    CONSTRAINT fk_val_sup FOREIGN KEY (id_superintendencia) REFERENCES cat_superintendencia(id),
    CONSTRAINT fk_val_em  FOREIGN KEY (id_emisor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_val_re  FOREIGN KEY (id_receptor) REFERENCES cat_responsables(id),
    CONSTRAINT fk_val_est FOREIGN KEY (id_estatus) REFERENCES cat_estatus_detalle(id),
    CONSTRAINT fk_val_emp FOREIGN KEY (id_empresa) REFERENCES cat_empresas(id)
);
CREATE TABLE valuaciones_documentos (
    id_valuacion INTEGER NOT NULL REFERENCES valuaciones(id_valuacion) ON DELETE CASCADE,
    id_documento INTEGER NOT NULL REFERENCES cat_documento(id),
    PRIMARY KEY (id_valuacion, id_documento)
);
CREATE INDEX idx_exp_solped              ON expedientes(solped);
CREATE INDEX idx_exp_gerencia            ON expedientes(id_gerencia);
CREATE INDEX idx_exp_estatus             ON expedientes(id_estatus);
CREATE INDEX idx_exp_empresa             ON expedientes(id_empresa);
CREATE INDEX idx_exp_fecha_presup        ON expedientes(fecha_presupuesto_base);
CREATE INDEX idx_exp_fecha_creacion      ON expedientes(fecha_creacion);
CREATE INDEX idx_exp_fecha_actualizacion ON expedientes(fecha_actualizacion);
CREATE INDEX idx_hist_mov_expediente     ON historial_movimientos(id_expediente);
CREATE INDEX idx_hist_mov_estatus        ON historial_movimientos(id_estatus);
CREATE INDEX idx_hist_mov_emisor         ON historial_movimientos(id_emisor);
CREATE INDEX idx_hist_mov_receptor       ON historial_movimientos(id_receptor);
CREATE INDEX idx_exp_doc_expediente      ON expediente_documentos(id_expediente);
CREATE INDEX idx_exp_doc_documento       ON expediente_documentos(id_documento);
CREATE TRIGGER trg_exp_auditoria AFTER UPDATE ON expedientes
FOR EACH ROW
WHEN (OLD.solped IS NOT NEW.solped OR OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.id_receptor IS NOT NEW.id_receptor OR OLD.id_plan IS NOT NEW.id_plan OR OLD.id_modalidad IS NOT NEW.id_modalidad OR OLD.id_art IS NOT NEW.id_art OR OLD.id_tipo_contrato IS NOT NEW.id_tipo_contrato OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.id_resultado IS NOT NEW.id_resultado OR OLD.id_empresa IS NOT NEW.id_empresa OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.fecha_devuelto IS NOT NEW.fecha_devuelto OR OLD.fecha_presupuesto_base IS NOT NEW.fecha_presupuesto_base OR OLD.fecha_firma_contrato IS NOT NEW.fecha_firma_contrato OR OLD.nro_proceso IS NOT NEW.nro_proceso OR OLD.nro_acta_apertura IS NOT NEW.nro_acta_apertura OR OLD.nro_resolucion_jd IS NOT NEW.nro_resolucion_jd OR OLD.nro_contrato_sicac IS NOT NEW.nro_contrato_sicac OR OLD.nro_contrato_sap IS NOT NEW.nro_contrato_sap OR OLD.descripcion_proceso IS NOT NEW.descripcion_proceso OR OLD.presupuesto_base_usd IS NOT NEW.presupuesto_base_usd OR OLD.presupuesto_base_bs IS NOT NEW.presupuesto_base_bs OR OLD.tipo_cambio IS NOT NEW.tipo_cambio OR OLD.monto_adjudicado_usd IS NOT NEW.monto_adjudicado_usd OR OLD.monto_adjudicado_bs IS NOT NEW.monto_adjudicado_bs OR OLD.tiempo_ejecucion IS NOT NEW.tiempo_ejecucion OR OLD.cantidad_frentes IS NOT NEW.cantidad_frentes OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas)
BEGIN
    INSERT INTO historial_movimientos (
        id_expediente, solped, id_gerencia, id_superintendencia,
        id_emisor, id_receptor,
        id_plan, id_modalidad, id_art, id_tipo_contrato, id_estatus,
        id_resultado, id_empresa, documentos,
        fecha_recibido, fecha_devuelto, fecha_presupuesto_base,
        fecha_firma_contrato,
        nro_proceso, nro_acta_apertura, nro_resolucion_jd,
        nro_contrato_sicac, nro_contrato_sap,
        descripcion_proceso,
        presupuesto_base_usd, presupuesto_base_bs, tipo_cambio,
        monto_adjudicado_usd, monto_adjudicado_bs,
        tiempo_ejecucion, cantidad_frentes,
        observaciones, notas
    ) VALUES (
        NEW.id_expediente, NEW.solped, NEW.id_gerencia, NEW.id_superintendencia,
        NEW.id_emisor, NEW.id_receptor,
        NEW.id_plan, NEW.id_modalidad, NEW.id_art, NEW.id_tipo_contrato, NEW.id_estatus,
        NEW.id_resultado, NEW.id_empresa,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '')
         FROM expediente_documentos ed
         JOIN cat_documento d ON ed.id_documento = d.id
         WHERE ed.id_expediente = NEW.id_expediente),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.fecha_presupuesto_base,
        NEW.fecha_firma_contrato,
        NEW.nro_proceso, NEW.nro_acta_apertura, NEW.nro_resolucion_jd,
        NEW.nro_contrato_sicac, NEW.nro_contrato_sap,
        NEW.descripcion_proceso,
        NEW.presupuesto_base_usd, NEW.presupuesto_base_bs, NEW.tipo_cambio,
        NEW.monto_adjudicado_usd, NEW.monto_adjudicado_bs,
        NEW.tiempo_ejecucion, NEW.cantidad_frentes,
        NEW.observaciones, NEW.notas
    );

    UPDATE expedientes
    SET id_estatus = 1
    WHERE NEW.fecha_firma_contrato IS NULL
      AND OLD.fecha_firma_contrato IS NOT NULL
      AND id_expediente = NEW.id_expediente;

    UPDATE expedientes
    SET id_estatus = 2
    WHERE NEW.fecha_firma_contrato IS NOT NULL
      AND OLD.fecha_firma_contrato IS NULL
      AND id_expediente = NEW.id_expediente;

    UPDATE expedientes
    SET fecha_actualizacion = CURRENT_TIMESTAMP
    WHERE id_expediente = NEW.id_expediente;
END;
CREATE TRIGGER trg_req_mat_inicial AFTER INSERT ON req_materiales
FOR EACH ROW BEGIN
    INSERT INTO hist_req_materiales (id_requisicion, id_gerencia, id_superintendencia, id_emisor, descripcion_materiales, serial_equipo, pase_sicesma, id_estatus, documentos, observaciones_entrega, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_requisicion, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.descripcion_materiales, NEW.serial_equipo, NEW.pase_sicesma, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM req_materiales_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_requisicion = NEW.id_requisicion),
        NEW.observaciones_entrega, NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
END;
CREATE TRIGGER trg_req_mat_auditoria AFTER UPDATE ON req_materiales
FOR EACH ROW
WHEN OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.descripcion_materiales IS NOT NEW.descripcion_materiales OR OLD.serial_equipo IS NOT NEW.serial_equipo OR OLD.pase_sicesma IS NOT NEW.pase_sicesma OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.observaciones_entrega IS NOT NEW.observaciones_entrega OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.fecha_devuelto IS NOT NEW.fecha_devuelto OR OLD.id_receptor IS NOT NEW.id_receptor OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas
BEGIN
    INSERT INTO hist_req_materiales (id_requisicion, id_gerencia, id_superintendencia, id_emisor, descripcion_materiales, serial_equipo, pase_sicesma, id_estatus, documentos, observaciones_entrega, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_requisicion, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.descripcion_materiales, NEW.serial_equipo, NEW.pase_sicesma, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM req_materiales_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_requisicion = NEW.id_requisicion),
        NEW.observaciones_entrega, NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
    UPDATE req_materiales SET fecha_actualizacion = CURRENT_TIMESTAMP WHERE id_requisicion = NEW.id_requisicion;
END;
CREATE INDEX idx_req_mat_estatus ON req_materiales(id_estatus);
CREATE INDEX idx_hist_req_mat_id ON hist_req_materiales(id_requisicion);
CREATE INDEX idx_req_doc_requisicion ON req_materiales_documentos(id_requisicion);
CREATE TRIGGER trg_mem_inicial AFTER INSERT ON memorandums
FOR EACH ROW BEGIN
    INSERT INTO hist_memorandums (id_memorandum, id_gerencia, id_superintendencia, id_emisor, asunto, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_memorandum, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.asunto, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM memorandums_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_memorandum = NEW.id_memorandum),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
END;
CREATE TRIGGER trg_mem_auditoria AFTER UPDATE ON memorandums
FOR EACH ROW
WHEN OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.asunto IS NOT NEW.asunto OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.fecha_devuelto IS NOT NEW.fecha_devuelto OR OLD.id_receptor IS NOT NEW.id_receptor OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas
BEGIN
    INSERT INTO hist_memorandums (id_memorandum, id_gerencia, id_superintendencia, id_emisor, asunto, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_memorandum, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.asunto, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM memorandums_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_memorandum = NEW.id_memorandum),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
    UPDATE memorandums SET fecha_actualizacion = CURRENT_TIMESTAMP WHERE id_memorandum = NEW.id_memorandum;
END;
CREATE INDEX idx_mem_estatus ON memorandums(id_estatus);
CREATE INDEX idx_hist_mem_id ON hist_memorandums(id_memorandum);
CREATE INDEX idx_mem_doc_memorandum ON memorandums_documentos(id_memorandum);
CREATE INDEX idx_val_estatus ON valuaciones(id_estatus);
CREATE INDEX idx_val_empresa ON valuaciones(id_empresa);
CREATE INDEX idx_hist_val_id ON hist_valuaciones(id_valuacion);
CREATE INDEX idx_val_doc_valuacion ON valuaciones_documentos(id_valuacion);
CREATE TRIGGER trg_jd_inicial AFTER INSERT ON aprobacion_jd
FOR EACH ROW BEGIN
    INSERT INTO hist_aprobacion_jd (id_aprobacion_jd, id_gerencia, id_superintendencia, id_emisor, solped, fecha_presupuesto_base, presupuesto_base_bs, tipo_cambio, presupuesto_base_usd, id_plan, descripcion_proceso, cantidad_frentes, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, tiempo_ejecucion, observaciones, notas)
    VALUES (NEW.id_aprobacion_jd, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.solped, NEW.fecha_presupuesto_base, NEW.presupuesto_base_bs, NEW.tipo_cambio, NEW.presupuesto_base_usd, NEW.id_plan, NEW.descripcion_proceso, NEW.cantidad_frentes, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM aprobacion_jd_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_aprobacion_jd = NEW.id_aprobacion_jd),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.tiempo_ejecucion, NEW.observaciones, NEW.notas);
END;
CREATE TRIGGER trg_jd_auditoria AFTER UPDATE ON aprobacion_jd
FOR EACH ROW
WHEN OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.solped IS NOT NEW.solped OR OLD.fecha_presupuesto_base IS NOT NEW.fecha_presupuesto_base OR OLD.presupuesto_base_bs IS NOT NEW.presupuesto_base_bs OR OLD.tipo_cambio IS NOT NEW.tipo_cambio OR OLD.presupuesto_base_usd IS NOT NEW.presupuesto_base_usd OR OLD.id_plan IS NOT NEW.id_plan OR OLD.descripcion_proceso IS NOT NEW.descripcion_proceso OR OLD.cantidad_frentes IS NOT NEW.cantidad_frentes OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.fecha_devuelto IS NOT NEW.fecha_devuelto OR OLD.id_receptor IS NOT NEW.id_receptor OR OLD.tiempo_ejecucion IS NOT NEW.tiempo_ejecucion OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas
BEGIN
    INSERT INTO hist_aprobacion_jd (id_aprobacion_jd, id_gerencia, id_superintendencia, id_emisor, solped, fecha_presupuesto_base, presupuesto_base_bs, tipo_cambio, presupuesto_base_usd, id_plan, descripcion_proceso, cantidad_frentes, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, tiempo_ejecucion, observaciones, notas)
    VALUES (NEW.id_aprobacion_jd, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.solped, NEW.fecha_presupuesto_base, NEW.presupuesto_base_bs, NEW.tipo_cambio, NEW.presupuesto_base_usd, NEW.id_plan, NEW.descripcion_proceso, NEW.cantidad_frentes, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM aprobacion_jd_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_aprobacion_jd = NEW.id_aprobacion_jd),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.tiempo_ejecucion, NEW.observaciones, NEW.notas);
    UPDATE aprobacion_jd SET fecha_actualizacion = CURRENT_TIMESTAMP WHERE id_aprobacion_jd = NEW.id_aprobacion_jd;
END;
CREATE INDEX idx_jd_estatus ON aprobacion_jd(id_estatus);
CREATE INDEX idx_hist_jd_id ON hist_aprobacion_jd(id_aprobacion_jd);
CREATE INDEX idx_jd_doc_aprobacion ON aprobacion_jd_documentos(id_aprobacion_jd);
CREATE TRIGGER trg_bdu_inicial AFTER INSERT ON certificacion_bdu
FOR EACH ROW BEGIN
    INSERT INTO hist_certificacion_bdu (id_certificacion_bdu, id_gerencia, id_superintendencia, id_emisor, presupuesto_base_total_usd, monto_adjudicado_total_usd, monto_contrato, monto_ejecutado, monto_pagado, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_certificacion_bdu, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.presupuesto_base_total_usd, NEW.monto_adjudicado_total_usd, NEW.monto_contrato, NEW.monto_ejecutado, NEW.monto_pagado, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM certificacion_bdu_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_certificacion_bdu = NEW.id_certificacion_bdu),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
END;
CREATE TRIGGER trg_bdu_auditoria AFTER UPDATE ON certificacion_bdu
FOR EACH ROW
WHEN OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.presupuesto_base_total_usd IS NOT NEW.presupuesto_base_total_usd OR OLD.monto_adjudicado_total_usd IS NOT NEW.monto_adjudicado_total_usd OR OLD.monto_contrato IS NOT NEW.monto_contrato OR OLD.monto_ejecutado IS NOT NEW.monto_ejecutado OR OLD.monto_pagado IS NOT NEW.monto_pagado OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.fecha_devuelto IS NOT NEW.fecha_devuelto OR OLD.id_receptor IS NOT NEW.id_receptor OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas
BEGIN
    INSERT INTO hist_certificacion_bdu (id_certificacion_bdu, id_gerencia, id_superintendencia, id_emisor, presupuesto_base_total_usd, monto_adjudicado_total_usd, monto_contrato, monto_ejecutado, monto_pagado, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_certificacion_bdu, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.presupuesto_base_total_usd, NEW.monto_adjudicado_total_usd, NEW.monto_contrato, NEW.monto_ejecutado, NEW.monto_pagado, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM certificacion_bdu_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_certificacion_bdu = NEW.id_certificacion_bdu),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
    UPDATE certificacion_bdu SET fecha_actualizacion = CURRENT_TIMESTAMP WHERE id_certificacion_bdu = NEW.id_certificacion_bdu;
END;
CREATE INDEX idx_bdu_estatus ON certificacion_bdu(id_estatus);
CREATE INDEX idx_hist_bdu_id ON hist_certificacion_bdu(id_certificacion_bdu);
CREATE INDEX idx_bdu_doc_certif ON certificacion_bdu_documentos(id_certificacion_bdu);
CREATE TRIGGER trg_vac_inicial AFTER INSERT ON vacaciones
FOR EACH ROW BEGIN
    INSERT INTO hist_vacaciones (id_vacacion, id_gerencia, id_superintendencia, id_emisor, anio, cantidad_dias, fecha_desde, fecha_hasta, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_vacacion, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.anio, NEW.cantidad_dias, NEW.fecha_desde, NEW.fecha_hasta, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM vacaciones_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_vacacion = NEW.id_vacacion),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
END;
CREATE TRIGGER trg_vac_auditoria AFTER UPDATE ON vacaciones
FOR EACH ROW
WHEN OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.anio IS NOT NEW.anio OR OLD.cantidad_dias IS NOT NEW.cantidad_dias OR OLD.fecha_desde IS NOT NEW.fecha_desde OR OLD.fecha_hasta IS NOT NEW.fecha_hasta OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.fecha_devuelto IS NOT NEW.fecha_devuelto OR OLD.id_receptor IS NOT NEW.id_receptor OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas
BEGIN
    INSERT INTO hist_vacaciones (id_vacacion, id_gerencia, id_superintendencia, id_emisor, anio, cantidad_dias, fecha_desde, fecha_hasta, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_vacacion, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.anio, NEW.cantidad_dias, NEW.fecha_desde, NEW.fecha_hasta, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM vacaciones_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_vacacion = NEW.id_vacacion),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
    UPDATE vacaciones SET fecha_actualizacion = CURRENT_TIMESTAMP WHERE id_vacacion = NEW.id_vacacion;
END;
CREATE INDEX idx_vac_estatus ON vacaciones(id_estatus);
CREATE INDEX idx_hist_vac_id ON hist_vacaciones(id_vacacion);
CREATE INDEX idx_vac_doc_vacacion ON vacaciones_documentos(id_vacacion);
CREATE TRIGGER trg_rep_inicial AFTER INSERT ON reposos_medicos
FOR EACH ROW BEGIN
    INSERT INTO hist_reposos_medicos (id_reposo_medico, id_gerencia, id_superintendencia, id_emisor, dias_periodo, fecha_desde, fecha_hasta, id_estatus, documentos, fecha_recibido, observaciones, notas)
    VALUES (NEW.id_reposo_medico, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.dias_periodo, NEW.fecha_desde, NEW.fecha_hasta, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM reposos_medicos_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_reposo_medico = NEW.id_reposo_medico),
        NEW.fecha_recibido, NEW.observaciones, NEW.notas);
END;
CREATE TRIGGER trg_rep_auditoria AFTER UPDATE ON reposos_medicos
FOR EACH ROW
WHEN OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.dias_periodo IS NOT NEW.dias_periodo OR OLD.fecha_desde IS NOT NEW.fecha_desde OR OLD.fecha_hasta IS NOT NEW.fecha_hasta OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas
BEGIN
    INSERT INTO hist_reposos_medicos (id_reposo_medico, id_gerencia, id_superintendencia, id_emisor, dias_periodo, fecha_desde, fecha_hasta, id_estatus, documentos, fecha_recibido, observaciones, notas)
    VALUES (NEW.id_reposo_medico, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.dias_periodo, NEW.fecha_desde, NEW.fecha_hasta, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM reposos_medicos_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_reposo_medico = NEW.id_reposo_medico),
        NEW.fecha_recibido, NEW.observaciones, NEW.notas);
    UPDATE reposos_medicos SET fecha_actualizacion = CURRENT_TIMESTAMP WHERE id_reposo_medico = NEW.id_reposo_medico;
END;
CREATE INDEX idx_rep_estatus ON reposos_medicos(id_estatus);
CREATE INDEX idx_hist_rep_id ON hist_reposos_medicos(id_reposo_medico);
CREATE INDEX idx_rep_doc_reposo ON reposos_medicos_documentos(id_reposo_medico);
CREATE INDEX idx_ruta_junta_hoja_numero
    ON ruta_procesos_junta(id_hoja, numero);
CREATE INDEX idx_ruta_semana_junta_numero
    ON ruta_procesos_junta_semana(id_junta, numero);
CREATE INDEX idx_ruta_proceso_junta_numero
    ON ruta_procesos_junta_proceso(id_junta, numero);
CREATE INDEX idx_ruta_cronograma_proceso_fecha
    ON ruta_procesos_cronograma(id_junta_proceso, fecha);
CREATE INDEX idx_ruta_junta_leyenda_junta_orden
    ON ruta_procesos_junta_leyenda(id_junta, orden);
CREATE INDEX idx_app_undo_entries_scope_id
    ON app_undo_entries(scope, id);
CREATE TRIGGER trg_val_inicial AFTER INSERT ON valuaciones
FOR EACH ROW BEGIN
    INSERT INTO hist_valuaciones (id_valuacion, id_gerencia, id_superintendencia, id_emisor, solped, presupuesto_base_bs, presupuesto_base_usd, tipo_cambio, descripcion_proceso, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, nro_proceso, nro_contrato_sicac, nro_contrato_sap, id_empresa, tiempo_ejecucion, monto_adjudicado_bs, monto_adjudicado_usd, periodo_valuacion_desde, periodo_valuacion_hasta, monto_valuacion, nro_proforma, observaciones, notas)
    VALUES (NEW.id_valuacion, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.solped, NEW.presupuesto_base_bs, NEW.presupuesto_base_usd, NEW.tipo_cambio, NEW.descripcion_proceso, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM valuaciones_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_valuacion = NEW.id_valuacion),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.nro_proceso, NEW.nro_contrato_sicac, NEW.nro_contrato_sap, NEW.id_empresa, NEW.tiempo_ejecucion, NEW.monto_adjudicado_bs, NEW.monto_adjudicado_usd, NEW.periodo_valuacion_desde, NEW.periodo_valuacion_hasta, NEW.monto_valuacion, NEW.nro_proforma, NEW.observaciones, NEW.notas);
END;
CREATE TRIGGER trg_val_auditoria AFTER UPDATE ON valuaciones
FOR EACH ROW
WHEN OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.solped IS NOT NEW.solped OR OLD.presupuesto_base_bs IS NOT NEW.presupuesto_base_bs OR OLD.presupuesto_base_usd IS NOT NEW.presupuesto_base_usd OR OLD.tipo_cambio IS NOT NEW.tipo_cambio OR OLD.descripcion_proceso IS NOT NEW.descripcion_proceso OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.fecha_devuelto IS NOT NEW.fecha_devuelto OR OLD.id_receptor IS NOT NEW.id_receptor OR OLD.nro_proceso IS NOT NEW.nro_proceso OR OLD.nro_contrato_sicac IS NOT NEW.nro_contrato_sicac OR OLD.nro_contrato_sap IS NOT NEW.nro_contrato_sap OR OLD.id_empresa IS NOT NEW.id_empresa OR OLD.tiempo_ejecucion IS NOT NEW.tiempo_ejecucion OR OLD.monto_adjudicado_bs IS NOT NEW.monto_adjudicado_bs OR OLD.monto_adjudicado_usd IS NOT NEW.monto_adjudicado_usd OR OLD.periodo_valuacion_desde IS NOT NEW.periodo_valuacion_desde OR OLD.periodo_valuacion_hasta IS NOT NEW.periodo_valuacion_hasta OR OLD.monto_valuacion IS NOT NEW.monto_valuacion OR OLD.nro_proforma IS NOT NEW.nro_proforma OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas
BEGIN
    INSERT INTO hist_valuaciones (id_valuacion, id_gerencia, id_superintendencia, id_emisor, solped, presupuesto_base_bs, presupuesto_base_usd, tipo_cambio, descripcion_proceso, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, nro_proceso, nro_contrato_sicac, nro_contrato_sap, id_empresa, tiempo_ejecucion, monto_adjudicado_bs, monto_adjudicado_usd, periodo_valuacion_desde, periodo_valuacion_hasta, monto_valuacion, nro_proforma, observaciones, notas)
    VALUES (NEW.id_valuacion, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.solped, NEW.presupuesto_base_bs, NEW.presupuesto_base_usd, NEW.tipo_cambio, NEW.descripcion_proceso, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM valuaciones_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_valuacion = NEW.id_valuacion),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.nro_proceso, NEW.nro_contrato_sicac, NEW.nro_contrato_sap, NEW.id_empresa, NEW.tiempo_ejecucion, NEW.monto_adjudicado_bs, NEW.monto_adjudicado_usd, NEW.periodo_valuacion_desde, NEW.periodo_valuacion_hasta, NEW.monto_valuacion, NEW.nro_proforma, NEW.observaciones, NEW.notas);
    UPDATE valuaciones SET fecha_actualizacion = CURRENT_TIMESTAMP WHERE id_valuacion = NEW.id_valuacion;
END;
CREATE INDEX idx_rec_estatus ON recobros(id_estatus);
CREATE INDEX idx_hist_rec_id ON hist_recobros(id_recobro);
CREATE INDEX idx_rec_doc_recobro ON recobros_documentos(id_recobro);
CREATE INDEX idx_ruta_cronograma_leyenda
    ON ruta_procesos_cronograma(id_leyenda);
CREATE INDEX idx_ruta_junta_leyenda_leyenda
    ON ruta_procesos_junta_leyenda(id_leyenda);
CREATE INDEX idx_papelera_modulo ON papelera(modulo);
CREATE INDEX idx_bd_hojas_activo ON bd_hojas(activo);
CREATE INDEX idx_expedientes_id_hoja ON expedientes(id_hoja);
CREATE INDEX idx_req_materiales_id_hoja ON req_materiales(id_hoja);
CREATE INDEX idx_memorandums_id_hoja ON memorandums(id_hoja);
CREATE INDEX idx_recobros_id_hoja ON recobros(id_hoja);
CREATE INDEX idx_valuaciones_id_hoja ON valuaciones(id_hoja);
CREATE INDEX idx_aprobacion_jd_id_hoja ON aprobacion_jd(id_hoja);
CREATE INDEX idx_certificacion_bdu_id_hoja ON certificacion_bdu(id_hoja);
CREATE INDEX idx_vacaciones_id_hoja ON vacaciones(id_hoja);
CREATE INDEX idx_reposos_medicos_id_hoja ON reposos_medicos(id_hoja);
CREATE TRIGGER trg_exp_snapshot_inicial AFTER INSERT ON expedientes
FOR EACH ROW
BEGIN
    INSERT INTO historial_movimientos (
        id_expediente, solped, id_gerencia, id_superintendencia,
        id_emisor, id_receptor,
        id_plan, id_modalidad, id_art, id_tipo_contrato, id_estatus,
        id_resultado, id_empresa, documentos,
        fecha_recibido, fecha_devuelto, fecha_presupuesto_base,
        fecha_firma_contrato,
        nro_proceso, nro_acta_apertura, nro_resolucion_jd,
        nro_contrato_sicac, nro_contrato_sap,
        descripcion_proceso,
        presupuesto_base_usd, presupuesto_base_bs, tipo_cambio,
        monto_adjudicado_usd, monto_adjudicado_bs,
        tiempo_ejecucion, cantidad_frentes,
        observaciones, notas
    ) VALUES (
        NEW.id_expediente, NEW.solped, NEW.id_gerencia, NEW.id_superintendencia,
        NEW.id_emisor, NEW.id_receptor,
        NEW.id_plan, NEW.id_modalidad, NEW.id_art, NEW.id_tipo_contrato,
        CASE WHEN NEW.fecha_firma_contrato IS NULL THEN 1 ELSE 2 END,
        NEW.id_resultado, NEW.id_empresa,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '')
         FROM expediente_documentos ed
         JOIN cat_documento d ON ed.id_documento = d.id
         WHERE ed.id_expediente = NEW.id_expediente),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.fecha_presupuesto_base,
        NEW.fecha_firma_contrato,
        NEW.nro_proceso, NEW.nro_acta_apertura, NEW.nro_resolucion_jd,
        NEW.nro_contrato_sicac, NEW.nro_contrato_sap,
        NEW.descripcion_proceso,
        NEW.presupuesto_base_usd, NEW.presupuesto_base_bs, NEW.tipo_cambio,
        NEW.monto_adjudicado_usd, NEW.monto_adjudicado_bs,
        NEW.tiempo_ejecucion, NEW.cantidad_frentes,
        NEW.observaciones, NEW.notas
    );

    UPDATE expedientes
    SET id_estatus = CASE WHEN NEW.fecha_firma_contrato IS NULL THEN 1 ELSE 2 END
    WHERE id_expediente = NEW.id_expediente
      AND NEW.id_estatus IS NULL;
END;
CREATE INDEX idx_exp_frentes_exp_orden
    ON expediente_frentes_adicionales(id_expediente, orden);
CREATE INDEX idx_exp_frentes_empresa
    ON expediente_frentes_adicionales(id_empresa);
CREATE VIEW vw_reporte_excel_contrataciones AS
SELECT
    e.id_expediente,
    e.id_hoja AS id_hoja,
    COALESCE(e.solped, 'NO APLICA')              AS solped,
    g.nombre                                     AS gerencia,
    s.nombre                                     AS superintendencia,
    emisor.nombre                                AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(e.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN e.documentos_texto
        WHEN TRIM(COALESCE(e.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || e.documentos_texto
    END AS documentos,
    e.fecha_presupuesto_base,
    e.presupuesto_base_usd,
    e.tipo_cambio,
    e.presupuesto_base_bs,
    p.nombre                                     AS plan_contrataciones,
    e.descripcion_proceso,
    m.nombre                                     AS modalidad_contratacion,
    a.nombre                                     AS art,
    tc.nombre                                    AS tipo_contrato,
    COALESCE(e.nro_acta_apertura, 'NO APLICA')   AS nro_acta_apertura,
    e.cantidad_frentes,
    COALESCE(e.nro_resolucion_jd, 'NO APLICA')   AS nro_resolucion_jd,
    COALESCE(ed.nombre, 'NO APLICA')             AS estatus_detalle,
    e.fecha_recibido,
    e.fecha_devuelto,
    COALESCE(receptor.nombre, 'NO APLICA')       AS receptor,
    COALESCE(e.nro_proceso, 'NO APLICA')         AS nro_proceso,
    COALESCE(rp.nombre, 'NO APLICA')             AS resultados_proceso,
    COALESCE(e.nro_contrato_sicac, 'NO APLICA')  AS nro_contrato_sicac,
    COALESCE(e.nro_contrato_sap, 'NO APLICA')    AS nro_contrato_sap,
    COALESCE(emp.nombre, 'NO APLICA')            AS empresa_adjudicada,
    e.tiempo_ejecucion,
    e.monto_adjudicado_bs,
    e.monto_adjudicado_usd,
    COALESCE(e.fecha_firma_contrato, 'NO APLICA') AS fecha_firma_contrato,
    e.observaciones,
    e.notas,
    e.fecha_creacion,
    e.fecha_actualizacion
FROM expedientes e
LEFT JOIN cat_gerencia g          ON e.id_gerencia         = g.id
LEFT JOIN cat_superintendencia s  ON e.id_superintendencia = s.id
LEFT JOIN cat_plan_contratacion p ON e.id_plan             = p.id
LEFT JOIN cat_modalidad m         ON e.id_modalidad        = m.id
LEFT JOIN cat_art a               ON e.id_art              = a.id
LEFT JOIN cat_tipo_contrato tc    ON e.id_tipo_contrato    = tc.id
LEFT JOIN cat_estatus_detalle ed  ON e.id_estatus          = ed.id
LEFT JOIN cat_resultado_proceso rp ON e.id_resultado       = rp.id
LEFT JOIN cat_empresas emp        ON e.id_empresa          = emp.id
LEFT JOIN cat_responsables emisor ON e.id_emisor           = emisor.id
LEFT JOIN cat_responsables receptor ON e.id_receptor       = receptor.id
LEFT JOIN (
    SELECT id_expediente, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM expediente_documentos ed
    JOIN cat_documento d ON ed.id_documento = d.id
    GROUP BY id_expediente
) d ON e.id_expediente = d.id_expediente;
CREATE VIEW vw_reporte_req_materiales AS
SELECT
    r.id_requisicion,
    r.id_hoja AS id_hoja,
    g.nombre AS gerencia,
    s.nombre AS superintendencia,
    em.nombre AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(r.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN r.documentos_texto
        WHEN TRIM(COALESCE(r.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || r.documentos_texto
    END AS documentos,
    r.descripcion_materiales,
    r.serial_equipo,
    r.pase_sicesma,
    COALESCE(ed.nombre, 'NO APLICA') AS estatus_detalle,
    r.observaciones_entrega,
    r.fecha_recibido,
    r.fecha_devuelto,
    COALESCE(re.nombre, 'NO APLICA') AS receptor,
    r.observaciones,
    r.notas,
    r.fecha_creacion,
    r.fecha_actualizacion
FROM req_materiales r
LEFT JOIN cat_gerencia g ON r.id_gerencia = g.id
LEFT JOIN cat_superintendencia s ON r.id_superintendencia = s.id
LEFT JOIN cat_responsables em ON r.id_emisor = em.id
LEFT JOIN cat_responsables re ON r.id_receptor = re.id
LEFT JOIN cat_estatus_detalle ed ON r.id_estatus = ed.id
LEFT JOIN (
    SELECT id_requisicion, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM req_materiales_documentos ed
    JOIN cat_documento d ON ed.id_documento = d.id
    GROUP BY id_requisicion
) d ON r.id_requisicion = d.id_requisicion;
CREATE VIEW vw_reporte_memorandums AS
SELECT
    m.id_memorandum,
    m.id_hoja AS id_hoja,
    g.nombre AS gerencia,
    s.nombre AS superintendencia,
    em.nombre AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(m.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN m.documentos_texto
        WHEN TRIM(COALESCE(m.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || m.documentos_texto
    END AS documentos,
    m.asunto,
    COALESCE(ed.nombre, 'NO APLICA') AS estatus_detalle,
    m.fecha_recibido,
    m.fecha_devuelto,
    COALESCE(re.nombre, 'NO APLICA') AS receptor,
    m.observaciones,
    m.notas,
    m.fecha_creacion,
    m.fecha_actualizacion
FROM memorandums m
LEFT JOIN cat_gerencia g ON m.id_gerencia = g.id
LEFT JOIN cat_superintendencia s ON m.id_superintendencia = s.id
LEFT JOIN cat_responsables em ON m.id_emisor = em.id
LEFT JOIN cat_responsables re ON m.id_receptor = re.id
LEFT JOIN cat_estatus_detalle ed ON m.id_estatus = ed.id
LEFT JOIN (
    SELECT id_memorandum, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM memorandums_documentos ed
    JOIN cat_documento d ON ed.id_documento = d.id
    GROUP BY id_memorandum
) d ON m.id_memorandum = d.id_memorandum;
CREATE VIEW vw_reporte_valuaciones AS
SELECT
    v.id_valuacion,
    v.id_hoja AS id_hoja,
    g.nombre AS gerencia,
    s.nombre AS superintendencia,
    em.nombre AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(v.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN v.documentos_texto
        WHEN TRIM(COALESCE(v.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || v.documentos_texto
    END AS documentos,
    v.solped,
    v.presupuesto_base_bs,
    v.presupuesto_base_usd,
    v.descripcion_proceso,
    COALESCE(ed.nombre, 'NO APLICA') AS estatus_detalle,
    v.fecha_recibido,
    v.fecha_devuelto,
    COALESCE(re.nombre, 'NO APLICA') AS receptor,
    v.nro_proceso,
    v.nro_contrato_sicac,
    v.nro_contrato_sap,
    COALESCE(emp.nombre, 'NO APLICA') AS empresa_adjudicada,
    v.tiempo_ejecucion,
    v.monto_adjudicado_bs,
    v.monto_adjudicado_usd,
    v.periodo_valuacion_desde,
    v.periodo_valuacion_hasta,
    v.monto_valuacion,
    v.nro_proforma,
    v.observaciones,
    v.notas,
    v.fecha_creacion,
    v.fecha_actualizacion
FROM valuaciones v
LEFT JOIN cat_gerencia g ON v.id_gerencia = g.id
LEFT JOIN cat_superintendencia s ON v.id_superintendencia = s.id
LEFT JOIN cat_responsables em ON v.id_emisor = em.id
LEFT JOIN cat_responsables re ON v.id_receptor = re.id
LEFT JOIN cat_estatus_detalle ed ON v.id_estatus = ed.id
LEFT JOIN cat_empresas emp ON v.id_empresa = emp.id
LEFT JOIN (
    SELECT id_valuacion, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM valuaciones_documentos ed
    JOIN cat_documento d ON ed.id_documento = d.id
    GROUP BY id_valuacion
) d ON v.id_valuacion = d.id_valuacion;
CREATE VIEW vw_reporte_aprobacion_jd AS
SELECT
    j.id_aprobacion_jd,
    j.id_hoja AS id_hoja,
    g.nombre AS gerencia,
    s.nombre AS superintendencia,
    em.nombre AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(j.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN j.documentos_texto
        WHEN TRIM(COALESCE(j.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || j.documentos_texto
    END AS documentos,
    j.solped,
    j.fecha_presupuesto_base,
    j.presupuesto_base_bs,
    j.tipo_cambio,
    j.presupuesto_base_usd,
    p.nombre AS plan_contrataciones,
    j.descripcion_proceso,
    j.cantidad_frentes,
    COALESCE(ed.nombre, 'NO APLICA') AS estatus_detalle,
    j.fecha_recibido,
    j.fecha_devuelto,
    COALESCE(re.nombre, 'NO APLICA') AS receptor,
    j.tiempo_ejecucion,
    j.observaciones,
    j.notas,
    j.fecha_creacion,
    j.fecha_actualizacion
FROM aprobacion_jd j
LEFT JOIN cat_gerencia g ON j.id_gerencia = g.id
LEFT JOIN cat_superintendencia s ON j.id_superintendencia = s.id
LEFT JOIN cat_responsables em ON j.id_emisor = em.id
LEFT JOIN cat_responsables re ON j.id_receptor = re.id
LEFT JOIN cat_estatus_detalle ed ON j.id_estatus = ed.id
LEFT JOIN cat_plan_contratacion p ON j.id_plan = p.id
LEFT JOIN (
    SELECT id_aprobacion_jd, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM aprobacion_jd_documentos ed
    JOIN cat_documento d ON ed.id_documento = d.id
    GROUP BY id_aprobacion_jd
) d ON j.id_aprobacion_jd = d.id_aprobacion_jd;
CREATE VIEW vw_reporte_certificacion_bdu AS
SELECT
    b.id_certificacion_bdu,
    b.id_hoja AS id_hoja,
    g.nombre AS gerencia,
    s.nombre AS superintendencia,
    em.nombre AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(b.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN b.documentos_texto
        WHEN TRIM(COALESCE(b.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || b.documentos_texto
    END AS documentos,
    b.presupuesto_base_total_usd,
    b.monto_adjudicado_total_usd,
    b.monto_contrato,
    b.monto_ejecutado,
    b.monto_pagado,
    COALESCE(ed.nombre, 'NO APLICA') AS estatus_detalle,
    b.fecha_recibido,
    b.fecha_devuelto,
    COALESCE(re.nombre, 'NO APLICA') AS receptor,
    b.observaciones,
    b.notas,
    b.fecha_creacion,
    b.fecha_actualizacion
FROM certificacion_bdu b
LEFT JOIN cat_gerencia g ON b.id_gerencia = g.id
LEFT JOIN cat_superintendencia s ON b.id_superintendencia = s.id
LEFT JOIN cat_responsables em ON b.id_emisor = em.id
LEFT JOIN cat_responsables re ON b.id_receptor = re.id
LEFT JOIN cat_estatus_detalle ed ON b.id_estatus = ed.id
LEFT JOIN (
    SELECT id_certificacion_bdu, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM certificacion_bdu_documentos ed
    JOIN cat_documento d ON ed.id_documento = d.id
    GROUP BY id_certificacion_bdu
) d ON b.id_certificacion_bdu = d.id_certificacion_bdu;
CREATE VIEW vw_reporte_vacaciones AS
SELECT
    v.id_vacacion,
    v.id_hoja AS id_hoja,
    g.nombre AS gerencia,
    s.nombre AS superintendencia,
    em.nombre AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(v.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN v.documentos_texto
        WHEN TRIM(COALESCE(v.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || v.documentos_texto
    END AS documentos,
    v.anio,
    v.cantidad_dias,
    v.fecha_desde,
    v.fecha_hasta,
    COALESCE(ed.nombre, 'NO APLICA') AS estatus_detalle,
    v.fecha_recibido,
    v.fecha_devuelto,
    COALESCE(re.nombre, 'NO APLICA') AS receptor,
    v.observaciones,
    v.notas,
    v.fecha_creacion,
    v.fecha_actualizacion
FROM vacaciones v
LEFT JOIN cat_gerencia g ON v.id_gerencia = g.id
LEFT JOIN cat_superintendencia s ON v.id_superintendencia = s.id
LEFT JOIN cat_responsables em ON v.id_emisor = em.id
LEFT JOIN cat_responsables re ON v.id_receptor = re.id
LEFT JOIN cat_estatus_detalle ed ON v.id_estatus = ed.id
LEFT JOIN (
    SELECT id_vacacion, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM vacaciones_documentos ed
    JOIN cat_documento d ON ed.id_documento = d.id
    GROUP BY id_vacacion
) d ON v.id_vacacion = d.id_vacacion;
CREATE VIEW vw_reporte_reposos_medicos AS
SELECT
    r.id_reposo_medico,
    r.id_hoja AS id_hoja,
    g.nombre AS gerencia,
    s.nombre AS superintendencia,
    em.nombre AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(r.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN r.documentos_texto
        WHEN TRIM(COALESCE(r.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || r.documentos_texto
    END AS documentos,
    r.dias_periodo,
    r.fecha_desde,
    r.fecha_hasta,
    COALESCE(ed.nombre, 'NO APLICA') AS estatus_detalle,
    r.fecha_recibido,
    r.observaciones,
    r.notas,
    r.fecha_creacion,
    r.fecha_actualizacion
FROM reposos_medicos r
LEFT JOIN cat_gerencia g ON r.id_gerencia = g.id
LEFT JOIN cat_superintendencia s ON r.id_superintendencia = s.id
LEFT JOIN cat_responsables em ON r.id_emisor = em.id
LEFT JOIN cat_estatus_detalle ed ON r.id_estatus = ed.id
LEFT JOIN (
    SELECT id_reposo_medico, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM reposos_medicos_documentos ed
    JOIN cat_documento d ON ed.id_documento = d.id
    GROUP BY id_reposo_medico
) d ON r.id_reposo_medico = d.id_reposo_medico;
CREATE TRIGGER trg_rec_inicial AFTER INSERT ON recobros
FOR EACH ROW BEGIN
    INSERT INTO hist_recobros (id_recobro, id_gerencia, id_superintendencia, id_emisor, asunto, fecha_inicio, fecha_final, fechas_adicionales, servicios, beneficios, nota_debito_reverso, costo_servicio_usd, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_recobro, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.asunto, NEW.fecha_inicio, NEW.fecha_final, NEW.fechas_adicionales, NEW.servicios, NEW.beneficios, NEW.nota_debito_reverso, NEW.costo_servicio_usd, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM recobros_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_recobro = NEW.id_recobro),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
END;
CREATE TRIGGER trg_rec_auditoria AFTER UPDATE ON recobros
FOR EACH ROW
WHEN OLD.id_gerencia IS NOT NEW.id_gerencia OR OLD.id_superintendencia IS NOT NEW.id_superintendencia OR OLD.id_emisor IS NOT NEW.id_emisor OR OLD.asunto IS NOT NEW.asunto OR OLD.fecha_inicio IS NOT NEW.fecha_inicio OR OLD.fecha_final IS NOT NEW.fecha_final OR OLD.fechas_adicionales IS NOT NEW.fechas_adicionales OR OLD.servicios IS NOT NEW.servicios OR OLD.beneficios IS NOT NEW.beneficios OR OLD.nota_debito_reverso IS NOT NEW.nota_debito_reverso OR OLD.costo_servicio_usd IS NOT NEW.costo_servicio_usd OR OLD.id_estatus IS NOT NEW.id_estatus OR OLD.fecha_recibido IS NOT NEW.fecha_recibido OR OLD.fecha_devuelto IS NOT NEW.fecha_devuelto OR OLD.id_receptor IS NOT NEW.id_receptor OR OLD.observaciones IS NOT NEW.observaciones OR OLD.notas IS NOT NEW.notas
BEGIN
    INSERT INTO hist_recobros (id_recobro, id_gerencia, id_superintendencia, id_emisor, asunto, fecha_inicio, fecha_final, fechas_adicionales, servicios, beneficios, nota_debito_reverso, costo_servicio_usd, id_estatus, documentos, fecha_recibido, fecha_devuelto, id_receptor, observaciones, notas)
    VALUES (NEW.id_recobro, NEW.id_gerencia, NEW.id_superintendencia, NEW.id_emisor, NEW.asunto, NEW.fecha_inicio, NEW.fecha_final, NEW.fechas_adicionales, NEW.servicios, NEW.beneficios, NEW.nota_debito_reverso, NEW.costo_servicio_usd, NEW.id_estatus,
        (SELECT COALESCE(GROUP_CONCAT(d.nombre, ' / '), '') FROM recobros_documentos ed JOIN cat_documento d ON ed.id_documento = d.id WHERE ed.id_recobro = NEW.id_recobro),
        NEW.fecha_recibido, NEW.fecha_devuelto, NEW.id_receptor, NEW.observaciones, NEW.notas);
    UPDATE recobros SET fecha_actualizacion = CURRENT_TIMESTAMP WHERE id_recobro = NEW.id_recobro;
END;
CREATE VIEW vw_reporte_recobros AS
SELECT
    r.id_recobro,
    r.id_hoja AS id_hoja,
    g.nombre AS gerencia,
    s.nombre AS superintendencia,
    em.nombre AS emisor,
    CASE
        WHEN TRIM(COALESCE(d.documentos, '')) = '' AND TRIM(COALESCE(r.documentos_texto, '')) = '' THEN 'NO APLICA'
        WHEN TRIM(COALESCE(d.documentos, '')) = '' THEN r.documentos_texto
        WHEN TRIM(COALESCE(r.documentos_texto, '')) = '' THEN TRIM(d.documentos)
        ELSE TRIM(d.documentos) || ' / ' || r.documentos_texto
    END AS documentos,
    r.asunto,
    r.fecha_inicio,
    r.fecha_final,
    r.fechas_adicionales,
    r.servicios,
    r.beneficios,
    r.nota_debito_reverso,
    r.costo_servicio_usd,
    COALESCE(ed.nombre, 'NO APLICA') AS estatus_detalle,
    r.fecha_recibido,
    r.fecha_devuelto,
    COALESCE(re.nombre, 'NO APLICA') AS receptor,
    r.observaciones,
    r.notas,
    r.fecha_creacion,
    r.fecha_actualizacion
FROM recobros r
LEFT JOIN cat_gerencia g ON r.id_gerencia = g.id
LEFT JOIN cat_superintendencia s ON r.id_superintendencia = s.id
LEFT JOIN cat_responsables em ON r.id_emisor = em.id
LEFT JOIN cat_responsables re ON r.id_receptor = re.id
LEFT JOIN cat_estatus_detalle ed ON r.id_estatus = ed.id
LEFT JOIN (
    SELECT id_recobro, GROUP_CONCAT(d.nombre, ' / ') AS documentos
    FROM recobros_documentos rd
    JOIN cat_documento d ON rd.id_documento = d.id
    GROUP BY id_recobro
) d ON d.id_recobro = r.id_recobro;
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('ruta_procesos_leyenda',14);
INSERT INTO "sqlite_sequence" VALUES('recobros',0);
INSERT INTO "sqlite_sequence" VALUES('hist_recobros',0);
INSERT INTO "sqlite_sequence" VALUES('bd_hojas',1);
INSERT INTO "sqlite_sequence" VALUES('historial_movimientos',0);
INSERT INTO "sqlite_sequence" VALUES('hist_aprobacion_jd',0);
INSERT INTO "sqlite_sequence" VALUES('hist_vacaciones',0);
INSERT INTO "sqlite_sequence" VALUES('hist_reposos_medicos',0);
INSERT INTO "sqlite_sequence" VALUES('hist_req_materiales',0);
INSERT INTO "sqlite_sequence" VALUES('hist_memorandums',0);
INSERT INTO "sqlite_sequence" VALUES('hist_valuaciones',0);
INSERT INTO "sqlite_sequence" VALUES('hist_certificacion_bdu',0);
COMMIT;
PRAGMA user_version=20;
